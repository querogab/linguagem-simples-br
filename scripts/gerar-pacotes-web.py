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
    "Use sempre que pedirem para revisar, simplificar, clarear ou facilitar um texto em PT-BR. "
    "Aplica Linguagem Simples a comunicados, editais, ofícios, FAQs, e-mails e manuais."
)
CONTAGEM_CANONICA = (
    "- **Contagens declaradas:** só informar quantidade de palavras, frases, itens ou "
    "redução percentual depois de conferir mecanicamente. Se não puder conferir, explicar "
    "a mudança sem número. Nunca estimar uma contagem."
)
CONTAGEM_GEMINI = (
    "- **Contagens declaradas:** não informar quantidade de palavras, frases ou redução "
    "percentual por iniciativa própria. Se o usuário pedir uma contagem, conferir "
    "mecanicamente; se não puder conferir, dizer isso e explicar a mudança sem número. "
    "Nunca estimar."
)
DADOS_CANONICOS = (
    "  - **Antipadrão:** não sugerir `23h59`, `18h`, `10/10`, `site X` ou equivalente "
    "quando o original não trouxe esse dado. Escrever `[horário a confirmar]`, "
    "`[data a confirmar]` e `[link ou local a confirmar]`."
)
DADOS_GEMINI = (
    "  - Se o original não trouxe o dado, a versão revisada, os avisos e os exemplos só "
    "podem mostrar o marcador entre colchetes. Não demonstrar formato com números, nomes, "
    "endereços ou links inventados.\n"
    "  - Antes de entregar, conferir cada data, horário, valor, endereço e link da saída "
    "contra o original ou o contexto fornecido. O que não tiver fonte deve virar marcador."
)
UTILIZAVEL_CANONICO = (
    "  - Em texto acionável, só marcar ✓ quando a ação, o acesso necessário (link, endereço "
    "ou localização) e o prazo completo estiverem no trecho ou em contexto adjacente "
    "fornecido pelo usuário. Não presumir informação ausente. Se faltar um desses elementos, "
    "marcar ✗ e dizer qual."
)
UTILIZAVEL_GEMINI = (
    f"{UTILIZAVEL_CANONICO}\n"
    "  - Enumerar todas as lacunas detectadas. Em instrução sobre formulário, conferir "
    "separadamente acesso ao formulário, data completa e horário-limite; não omitir uma "
    "lacuna porque outra já justificou o ✗."
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


def substituir_unico(texto, original, substituto, rotulo):
    if texto.count(original) != 1:
        raise ValueError(f"Gemini: trecho canônico inesperado para {rotulo}.")
    return texto.replace(original, substituto)


def criar_skill_gemini(skill_canonica, destino):
    texto = skill_canonica.decode("utf-8")
    texto = substituir_unico(texto, CONTAGEM_CANONICA, CONTAGEM_GEMINI, "contagens")
    texto = substituir_unico(texto, DADOS_CANONICOS, DADOS_GEMINI, "dados ausentes")
    texto = substituir_unico(texto, UTILIZAVEL_CANONICO, UTILIZAVEL_GEMINI, "utilizável")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8", newline="\n")


def validar_pacotes(
    canonicos, corpo, pacote_claude, skill_gemini, pacote_chatgpt, pacote_plugin
):
    raiz = f"{NOME}/"

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

    frontmatter_gemini, _ = separar_skill(skill_gemini.read_bytes())
    if campo(frontmatter_gemini, "name") != NOME:
        raise ValueError("Gemini: nome da skill divergente.")
    if campo(frontmatter_gemini, "version") != campo(
        separar_skill(canonicos["SKILL.md"])[0], "version"
    ):
        raise ValueError("Gemini: versão da skill divergente.")
    texto_gemini = skill_gemini.read_text(encoding="utf-8")
    if any(valor in texto_gemini for valor in ("23h59", "18h", "10/10", "site X")):
        raise ValueError("Gemini: exemplo indutor permaneceu no arquivo gerado.")


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
    (args.saida / f"{NOME}-gemini-web-{versao}.zip").unlink(missing_ok=True)
    pacote_claude = args.saida / f"{NOME}-claude-web-cowork-{versao}.zip"
    skill_gemini = args.saida / "gemini-web" / "SKILL.md"
    pacote_chatgpt = args.saida / f"{NOME}-chatgpt-skill-{versao}.zip"
    pacote_plugin = args.saida / f"{NOME}-chatgpt-plugin-{versao}.zip"

    criar_zip(pacote_chatgpt, com_prefixo(canonicos, NOME))
    criar_skill_gemini(canonicos["SKILL.md"], skill_gemini)

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
        canonicos, corpo, pacote_claude, skill_gemini, pacote_chatgpt, pacote_plugin
    )

    pacotes = [pacote_claude, pacote_chatgpt, pacote_plugin]
    artefatos = [pacote_claude, skill_gemini, pacote_chatgpt, pacote_plugin]
    checksums = "".join(
        f"{sha256_bytes(artefato.read_bytes())}  "
        f"{artefato.relative_to(args.saida).as_posix()}\n"
        for artefato in artefatos
    )
    (args.saida / "SHA256SUMS.txt").write_text(checksums, encoding="ascii", newline="\n")

    print(f"Fonte: {FONTE}")
    print(f"Versão: {versao}")
    for pacote in pacotes:
        print(f"OK {pacote.name} ({len(ler_zip(pacote))} arquivos)")
    print("OK gemini-web/SKILL.md")
    print("OK SHA256SUMS.txt")


if __name__ == "__main__":
    main()
