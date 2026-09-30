#!/usr/bin/env python3
"""Gera e valida pacotes de upload sem duplicar a fonte da skill."""

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


RAIZ = Path(__file__).resolve().parents[1]
FONTE = RAIZ / ".agents" / "skills" / "linguagem-simples-br"
NOME = "linguagem-simples-br"
DESCRICAO_CLAUDE = (
    "Revisa e reescreve textos em Linguagem Simples em português do Brasil. "
    "Use em comunicados, editais, ofícios, FAQs, e-mails, manuais e materiais educativos."
)
DATA_ZIP = (2026, 9, 30, 0, 0, 0)
RE_FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def sha256_bytes(conteudo):
    return hashlib.sha256(conteudo).hexdigest()


def arquivos(pasta):
    encontrados = {}
    for item in sorted(pasta.rglob("*")):
        if item.is_symlink():
            raise ValueError(f"Link simbólico não permitido no pacote: {item}")
        if item.is_file():
            encontrados[item.relative_to(pasta).as_posix()] = item.read_bytes()
    return encontrados


def separar_skill(conteudo):
    texto = conteudo.decode("utf-8")
    match = RE_FRONTMATTER.match(texto)
    if not match:
        raise ValueError("SKILL.md sem frontmatter YAML delimitado por ---.")
    return match.group(1), texto[match.end() :]


def campo(frontmatter, nome):
    match = re.search(rf"^\s*{re.escape(nome)}:\s*['\"]?([^'\"\n]+)", frontmatter, re.MULTILINE)
    if not match:
        raise ValueError(f"Campo ausente no frontmatter: {nome}")
    return match.group(1).strip()


def criar_zip(destino, conteudos):
    with zipfile.ZipFile(destino, "w") as pacote:
        for caminho, conteudo in sorted(conteudos.items()):
            info = zipfile.ZipInfo(caminho, DATA_ZIP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            pacote.writestr(info, conteudo)


def ler_zip(caminho):
    with zipfile.ZipFile(caminho) as pacote:
        erro = pacote.testzip()
        if erro:
            raise ValueError(f"Arquivo corrompido no ZIP: {erro}")
        resultado = {}
        for nome in pacote.namelist():
            parte = PurePosixPath(nome)
            if parte.is_absolute() or ".." in parte.parts or "\\" in nome:
                raise ValueError(f"Caminho inseguro no ZIP: {nome}")
            if nome.endswith("/"):
                continue
            resultado[nome] = pacote.read(nome)
        return resultado


def com_prefixo(conteudos, prefixo):
    return {f"{prefixo}/{caminho}": conteudo for caminho, conteudo in conteudos.items()}


def validar_igualdade(referencia, recebido, rotulo):
    if referencia.keys() != recebido.keys():
        faltam = sorted(referencia.keys() - recebido.keys())
        sobram = sorted(recebido.keys() - referencia.keys())
        raise ValueError(f"{rotulo}: árvore divergente; faltam={faltam}; sobram={sobram}")
    diferentes = [nome for nome in referencia if referencia[nome] != recebido[nome]]
    if diferentes:
        raise ValueError(f"{rotulo}: arquivos divergentes: {diferentes}")


def validar_pacotes(
    canonicos, corpo, pacote_claude, pacote_gemini, pacote_chatgpt, pacote_plugin
):
    raiz = f"{NOME}/"

    validar_igualdade(canonicos, ler_zip(pacote_gemini), "Gemini web")

    chatgpt = ler_zip(pacote_chatgpt)
    chatgpt_skill = {
        nome.removeprefix(raiz): conteudo
        for nome, conteudo in chatgpt.items()
        if nome.startswith(raiz)
    }
    validar_igualdade(canonicos, chatgpt_skill, "ChatGPT Skill")

    plugin = ler_zip(pacote_plugin)
    manifest = json.loads(plugin.pop("plugin.json").decode("utf-8"))
    if manifest.get("name") != NOME or manifest.get("version") != campo(
        separar_skill(canonicos["SKILL.md"])[0], "version"
    ):
        raise ValueError("Plugin ChatGPT com nome ou versão divergente.")
    prefixo_plugin = f"skills/{NOME}/"
    plugin_skill = {
        nome.removeprefix(prefixo_plugin): conteudo
        for nome, conteudo in plugin.items()
        if nome.startswith(prefixo_plugin)
    }
    validar_igualdade(canonicos, plugin_skill, "ChatGPT Plugin")

    claude = ler_zip(pacote_claude)
    esperado_claude = {f"{raiz}{nome}": conteudo for nome, conteudo in canonicos.items()}
    esperado_claude.pop(f"{raiz}SKILL.md")
    skill_claude = claude.get(f"{raiz}skill.md")
    if skill_claude is None:
        raise ValueError("Claude: skill.md ausente.")
    frontmatter_claude, corpo_claude = separar_skill(skill_claude)
    if campo(frontmatter_claude, "name") != NOME:
        raise ValueError("Claude: nome da skill divergente.")
    if len(campo(frontmatter_claude, "description")) > 200:
        raise ValueError("Claude: descrição excede 200 caracteres.")
    if corpo_claude != corpo:
        raise ValueError("Claude: corpo da skill divergiu da fonte canônica.")
    for nome, conteudo in esperado_claude.items():
        if claude.get(nome) != conteudo:
            raise ValueError(f"Claude: recurso divergente ou ausente: {nome}")
    if set(claude) != set(esperado_claude) | {f"{raiz}skill.md"}:
        raise ValueError("Claude: árvore contém arquivo inesperado.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--saida",
        type=Path,
        default=RAIZ / "dist",
        help="Pasta de saída. Padrão: dist/ na raiz do projeto.",
    )
    args = parser.parse_args()

    if not FONTE.is_dir():
        raise SystemExit(f"Fonte canônica não encontrada: {FONTE}")
    canonicos = arquivos(FONTE)
    if "SKILL.md" not in canonicos:
        raise SystemExit("Fonte canônica sem SKILL.md.")

    frontmatter, corpo = separar_skill(canonicos["SKILL.md"])
    if campo(frontmatter, "name") != NOME:
        raise SystemExit("O nome do frontmatter não corresponde à pasta canônica.")
    versao = campo(frontmatter, "version")

    args.saida.mkdir(parents=True, exist_ok=True)
    pacote_claude = args.saida / f"{NOME}-claude-web-cowork-{versao}.zip"
    pacote_gemini = args.saida / f"{NOME}-gemini-web-{versao}.zip"
    pacote_chatgpt = args.saida / f"{NOME}-chatgpt-skill-{versao}.zip"
    pacote_plugin = args.saida / f"{NOME}-chatgpt-plugin-{versao}.zip"

    criar_zip(pacote_gemini, canonicos)
    criar_zip(pacote_chatgpt, com_prefixo(canonicos, NOME))

    claude = dict(canonicos)
    claude.pop("SKILL.md")
    skill_claude = (
        "---\n"
        f"name: {NOME}\n"
        f"description: {DESCRICAO_CLAUDE}\n"
        "---\n"
        f"{corpo}"
    ).encode("utf-8")
    claude["skill.md"] = skill_claude
    criar_zip(pacote_claude, com_prefixo(claude, NOME))

    manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": NOME,
        "version": versao,
        "description": "Revisão de textos em Linguagem Simples no português do Brasil.",
        "author": {"name": "Gabriela Quero"},
        "homepage": "https://github.com/querogab/linguagem-simples-br",
        "repository": "https://github.com/querogab/linguagem-simples-br",
        "license": "MIT",
        "keywords": ["linguagem-simples", "pt-br", "revisao"],
    }
    plugin = com_prefixo(canonicos, f"skills/{NOME}")
    plugin["plugin.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode(
        "utf-8"
    )
    criar_zip(pacote_plugin, plugin)

    validar_pacotes(
        canonicos,
        corpo,
        pacote_claude,
        pacote_gemini,
        pacote_chatgpt,
        pacote_plugin,
    )

    pacotes = [pacote_claude, pacote_gemini, pacote_chatgpt, pacote_plugin]
    checksums = "".join(
        f"{sha256_bytes(pacote.read_bytes())}  {pacote.name}\n" for pacote in pacotes
    )
    (args.saida / "SHA256SUMS.txt").write_text(checksums, encoding="ascii", newline="\n")

    print(f"Fonte: {FONTE}")
    print(f"Versão: {versao}")
    for pacote in pacotes:
        print(f"OK {pacote.name} ({len(ler_zip(pacote))} arquivos)")
    print("OK SHA256SUMS.txt")


if __name__ == "__main__":
    main()
