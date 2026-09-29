# -*- coding: utf-8 -*-
"""
medir.py — instrumento DESCRITIVO para comparar textos em PT-BR antes/depois.

⚠️ LEIA ANTES DE USAR
Isto NÃO é uma nota de qualidade e NÃO deve virar alvo de otimização.
O [relatório de auditoria do SimpleEnglish](https://github.com/AminBlg/SimpleEnglish/blob/main/evals/results/WHY-USELESS-2026-09-02.md) documenta exatamente esse fracasso:
a skill passou a otimizar para o próprio linter e piorou para o leitor.
Use estes números como DESCRIÇÃO ao lado da leitura humana, nunca no lugar dela.

O que mede: distribuição de tamanho de frase, nominalizações, marcas de voz
passiva, conectivos de burocratês, siglas não expandidas e palavras-esquiva.

Uso:
    python medir.py arquivo.txt [arquivo2.txt ...]
    python medir.py --json arquivo.txt        # saída JSON para diff posterior
"""
import re, sys, json, io, os

# --- listas: derivadas da tabela de trocas da skill + anti-padrões da §3.1 do plano ---
NOMINALIZACOES = [
    'realização de', 'efetivação de', 'elaboração de', 'manutenção de', 'análise de',
    'avaliação de', 'disponibilização de', 'utilização de', 'implementação de',
    'aplicação de', 'execução de', 'apresentação de', 'divulgação de', 'prestação de',
    'observância de', 'cumprimento de', 'atendimento de', 'expedição de',
]
CONECTIVOS = [
    'no que diz respeito a', 'no que tange a', 'no que concerne a', 'em virtude de',
    'em razão de', 'em decorrência de', 'no âmbito de', 'a fim de', 'com o intuito de',
    'com vistas a', 'por meio de', 'através de', 'no sentido de', 'em face de',
    'a partir do momento em que', 'caso venha a', 'diante do exposto', 'cumpre-nos',
    'cabe-nos', 'consoante', 'conforme disposto em', 'sem prejuízo de', 'à luz de',
    'nos termos de', 'ressalvado o disposto',
]
ESQUIVA = [
    'acredita-se que', 'entende-se que', 'potencialmente', 'de certa forma',
    'supostamente', 'eventualmente', 'em tese', 'a princípio', 'de modo geral',
    'em tempo hábil', 'brevemente', 'oportunamente', 'tão logo possível',
]
# marcas de passiva analitica: ser/estar + particípio (-ado/-ido/-to/-so)
PASSIVA = re.compile(
    r'\b(é|são|foi|foram|será|serão|seja|sejam|está|estão|fosse|fossem|sendo|ser)\s+'
    r'(\w+(?:ado|ada|ados|adas|ido|ida|idos|idas|to|ta|tos|tas|so|sa|sos|sas))\b', re.I)
# passiva sintetica: verbo + "-se" em contexto normativo
PASSIVA_SE = re.compile(r'\b\w+(?:a|e|i)-se\b', re.I)
SIGLA = re.compile(r'\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,8}\b')
# Numeral romano de inciso NÃO é sigla. Falso positivo encontrado pelo controle
# positivo em 04/09/26 — o instrumento acusava "II, III, IV, IX" como siglas a
# expandir em texto legal. Controle serve para isso.
ROMANO = re.compile(r'^[IVXLCDM]+$')
ABREV_OK = {'CPF', 'CNPJ', 'DOU', 'PT', 'BR', 'LS', 'ISO', 'ABNT', 'NBR',
            'VETADO', 'DE', 'DO', 'DA', 'DAS', 'DOS', 'EM', 'NO', 'NA', 'AO'}


# Markdown NAO e prosa. Linha de tabela nao tem pontuacao de fim, entao o
# segmentador leu tabelas inteiras como UMA frase: a rodada de 04/09/26 gerou
# "frases" de 212, 210, 155 e 108 palavras, e a comparacao skill x micro virou
# uma medida de FORMATO DE SAIDA, nao de prosa. Quem entrega tabela era punido;
# quem entrega texto corrido, premiado. Defeito do instrumento, nao do texto.
RE_TABELA = re.compile(r'^\s*\|.*\|\s*$', re.M)
RE_TITULO = re.compile(r'^\s{0,3}#{1,6}\s.*$', re.M)
# 05/09/26: subtitulo so em negrito (**Assim**) e linha de metadado (**Campo:** valor)
# nao eram descartados e colavam na frase seguinte -- deram 'frases' de 45 e 56 palavras.
RE_NEGRITO  = re.compile(r'^[ \t]{0,3}\*\*[^*\n]{1,120}\*\*[ \t]*$', re.M)
RE_METADADO = re.compile(r'^[ \t]{0,3}\*\*[^*\n]{1,40}:\*\*[^\n]*$', re.M)
# 06/09/26: a regra horizontal (---) NAO era descartada: o padrao carregava dois
# bytes de controle  invisiveis (^\s*([-*_])\s*\s*[-*_\s]*$) e a regex
# nunca casava com nada. O --- colava na frase seguinte. Achado pelo CTRL-MD na
# PRIMEIRA execucao dele -- e tinha DIRECAO: so a condicao skill entrega ---.
RE_REGRA = re.compile(r'^[ \t]*(?:-{3,}|\*{3,}|_{3,})[ \t]*$', re.M)
RE_CERCA = re.compile(r'^```.*?^```', re.M | re.S)


def limpar_markdown(t):
    """Tira o que nao e prosa e devolve (texto, quantos blocos foram tirados).
    Sempre relatar o descartado: medicao silenciosa de coisa errada e pior
    do que medicao nenhuma."""
    tirados = 0
    for rx in (RE_CERCA, RE_TABELA, RE_TITULO, RE_NEGRITO, RE_METADADO, RE_REGRA):
        achados = rx.findall(t)
        tirados += len(achados)
        t = rx.sub(' ', t)
    t = re.sub(r'[*_`>]+', ' ', t)          # enfase e citacao
    # Item de lista sem ponto final e uma unidade que o leitor le sozinha.
    # Sem fechar, o segmentador cola a lista inteira numa "frase" de 164
    # palavras - achado do sinalizador >60 em 05/09/26. So mexe em item de
    # lista de markdown; prosa em .txt nao e tocada.
    def _fecha_item(mo):
        corpo = mo.group(2).rstrip()
        return corpo if corpo.endswith(('.', ';', ':', '!', '?')) else corpo + '.'
    # 05/09/26: item com LETRA ou ROMANO tambem fecha frase. Sem isto, o edital T7
    # virou 'frase' de 110 palavras -- eram a) b) c) colados.
    t = re.sub(r'^[ 	]*([-+*]|\d{1,3}[.)]|[a-z][.)]|[ivxIVX]{1,4}[.)])[ 	]+(.*)$', _fecha_item, t, flags=re.M)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', lambda m: m.group(1), t)  # 06/09/26: o link agora vira MESMO o rotulo. O comentario dizia isso e o codigo apagava o rotulo junto com o endereco.
    return t, tirados


def frases(t):
    """Segmenta por pontuação forte. Ponto-e-vírgula conta como fronteira:
    em texto legal ele separa incisos, que o leitor lê como unidades."""
    partes = re.split(r'(?<=[.;:!?])\s+', t)
    return [p.strip() for p in partes if len(p.split()) >= 2]


def conta_termos(t, termos):
    baixo = t.lower()
    achados = {}
    for termo in termos:
        n = baixo.count(termo)
        if n:
            achados[termo] = n
    return achados


def medir(texto, nome=''):
    texto, blocos_md = limpar_markdown(texto)
    t = re.sub(r'\s+', ' ', texto).strip()
    pal = t.split()
    fr = frases(t)
    tam = sorted(len(f.split()) for f in fr) or [0]
    n = len(tam)

    def pct(k):
        return round(100.0 * k / n, 1) if n else 0.0

    nomin = conta_termos(t, NOMINALIZACOES)
    conec = conta_termos(t, CONECTIVOS)
    esq = conta_termos(t, ESQUIVA)
    passivas = PASSIVA.findall(t)
    passivas_se = PASSIVA_SE.findall(t)
    siglas = sorted({s for s in SIGLA.findall(t)
                     if s not in ABREV_OK and not ROMANO.match(s)})

    return {
        'arquivo': nome,
        'blocos_markdown_descartados': blocos_md,
        'frases_suspeitas_acima_60': sum(1 for x in tam if x > 60),
        'palavras': len(pal),
        'frases': n,
        'tam_medio': round(sum(tam) / n, 1) if n else 0,
        'tam_mediana': tam[n // 2] if n else 0,
        'tam_max': tam[-1] if n else 0,
        'pct_acima_25': pct(sum(1 for x in tam if x > 25)),
        'pct_acima_30': pct(sum(1 for x in tam if x > 30)),
        'nominalizacoes': sum(nomin.values()),
        'nominalizacoes_quais': nomin,
        'conectivos_burocraticos': sum(conec.values()),
        'conectivos_quais': conec,
        'palavras_esquiva': sum(esq.values()),
        'palavras_esquiva_quais': esq,
        'passiva_analitica': len(passivas),
        'passiva_se': len(passivas_se),
        'siglas_candidatas': siglas,
        # densidade por 100 palavras — a única forma de comparar textos de tamanhos diferentes
        'por100_nominalizacao': round(100.0 * sum(nomin.values()) / max(len(pal), 1), 2),
        'por100_conectivo': round(100.0 * sum(conec.values()) / max(len(pal), 1), 2),
        'por100_passiva': round(100.0 * (len(passivas) + len(passivas_se)) / max(len(pal), 1), 2),
    }


def imprimir(m):
    print('\n=== %s ===' % (m['arquivo'] or 'texto'))
    print('  %d palavras · %d frases · média %.1f · mediana %d · máx %d'
          % (m['palavras'], m['frases'], m['tam_medio'], m['tam_mediana'], m['tam_max']))
    print('  frases > 25 palavras: %s%%   > 30: %s%%' % (m['pct_acima_25'], m['pct_acima_30']))
    print('  por 100 palavras — nominalização %.2f · conectivo burocrático %.2f · passiva %.2f'
          % (m['por100_nominalizacao'], m['por100_conectivo'], m['por100_passiva']))
    if m['blocos_markdown_descartados']:
        print('  (%d blocos de markdown descartados antes de medir)' % m['blocos_markdown_descartados'])
    if m['frases_suspeitas_acima_60']:
        print('  !! %d "frase(s)" acima de 60 palavras - quase sempre e estrutura, nao prosa. CONFERIR.'
              % m['frases_suspeitas_acima_60'])
    if m['nominalizacoes_quais']:
        print('  nominalizações: %s' % ', '.join('%s(%d)' % kv for kv in m['nominalizacoes_quais'].items()))
    if m['conectivos_quais']:
        print('  conectivos: %s' % ', '.join('%s(%d)' % kv for kv in m['conectivos_quais'].items()))
    if m['palavras_esquiva_quais']:
        print('  esquiva: %s' % ', '.join('%s(%d)' % kv for kv in m['palavras_esquiva_quais'].items()))
    if m['siglas_candidatas']:
        print('  siglas a conferir: %s' % ', '.join(m['siglas_candidatas'][:12]))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--json']
    saida_json = '--json' in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    todos = []
    for caminho in args:
        txt = io.open(caminho, encoding='utf-8').read()
        m = medir(txt, os.path.basename(caminho))
        todos.append(m)
        if not saida_json:
            imprimir(m)
    if saida_json:
        print(json.dumps(todos, ensure_ascii=False, indent=2))
