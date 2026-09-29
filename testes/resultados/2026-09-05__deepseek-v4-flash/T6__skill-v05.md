**Arquivo:** T6__manual-mcasp.txt
**Condição:** skill (v0.5)
**Modelo:** deepseek/deepseek-v4-flash

---

## Passo 1 — Planejamento

**Inferência do contexto:** Texto do MCASP (Manual de Contabilidade Aplicada ao Setor Público), documento técnico-contábil do Tesouro Nacional. Contexto: **órgão público** — LS obrigatória pela Lei 15.263/2025. Público: contadores públicos, auditores, gestores financeiros. NÃO é cidadão comum — é texto técnico especializado. Objetivo: explicar procedimentos contábeis patrimoniais.

Confirmado: público técnico (contadores do setor público). LS deve simplificar a forma sem trair a precisão contábil. Termos técnicos como "CEC", "ativo financeiro", "superavit financeiro" são do domínio do público-alvo — manter.

## Passo 2 — Diagnóstico

1. **(A1) Nariz de cera:** "MCASP 2023 / Parte II - Procedimentos Contábeis Patrimoniais" — o título é informação estrutural, não nariz de cera. Mantido.
2. **(A5) Verbos substantivados:** "aplicação subsidiária", "enquadramento", "apuração", "segregação".
3. **(C1) Frases longas:** parágrafo 4.3.3 tem frases de 55+ palavras com várias camadas de subordinação.
4. **(C2) Voz passiva sem motivo:** "são classificáveis", "deve ser registrado", "entende-se que".
5. **(C4) Frases intercaladas:** "Quanto ao requisito de risco insignificante de mudança de valor entende-se que classificar..." — estrutura com intercalação confusa.
6. **(A6) Jargão sem explicação:** "pré-fixadas ou pós-fixadas", "custo amortizado ou valor justo" — ok para público contábil, mas poderiam ter breve contextualização.
7. **(B2) Mais de uma ideia por parágrafo:** parágrafo 4.3.3 mistura definição de CEC + discussão sobre risco + mensuração.

## Passo 3 — Heurística

Texto com ~450 palavras. Entre 301 e 1.000: reescrever os trechos mais problemáticos (parágrafos 4.3.3 e 4.4).

## Passo 4 — Reescrita

**Freio de sobre-edição:** termos técnicos contábeis (CEC, superávit financeiro, ativo financeiro/passivo financeiro) mantidos — são o vocabulário do público. Artigos de lei transcritos literalmente mantidos. 3 parágrafos revisados; 2 frases mantidas intactas (citações legais).

### Versão final limpa

**MCASP 2023 — Parte II: Procedimentos Contábeis Patrimoniais**

**Depósitos Bancários Vinculados**

Depósitos bancários vinculados não devem entrar no saldo das Disponibilidades. No Balanço, eles são classificados em conta separada, no Ativo Circulante ou no Realizável a Longo Prazo, como créditos e valores a receber. A classificação leva em conta as características específicas de cada depósito e as restrições que existem sobre ele.

**4.3.3. Aplicações Financeiras**

Para que uma aplicação financeira seja classificada como Caixa e Equivalentes de Caixa (CEC), ela precisa:
- servir para pagar compromissos de caixa de curto prazo (não investimento nem outros fins)
- ser conversível rapidamente em uma quantia conhecida de caixa, no curto prazo
- ter risco insignificante de mudança de valor

Sobre o risco: classificar a aplicação como pré-fixada ou pós-fixada não define o nível de risco. Os dois tipos estão expostos à volatilidade do mercado. Por isso, essa distinção não determina se a aplicação deve ser medida pelo custo amortizado ou pelo valor justo.

Os rendimentos das aplicações financeiras de liquidez imediata (classificadas como equivalentes de caixa) acompanham o principal. Eles devem ser registrados de forma a somar-se ao saldo dos valores disponíveis, ou seja, no grupo de contas de CEC.

**4.4. Aspectos Orçamentários**

A Lei nº 4.320/64 define o conceito de ativo financeiro para o cálculo do superávit financeiro. O superávit financeiro é a fonte para abertura de créditos adicionais.

O Art. 43 trata do superávit financeiro:
> § 2º Entende-se por superávit financeiro a diferença positiva entre o ativo financeiro e o passivo financeiro, conjugando-se, ainda, os saldos dos créditos adicionais transferidos e as operações de crédito a eles vinculadas.

O Art. 105 trata da classificação dos ativos:
> § 1º O Ativo Financeiro compreenderá os créditos e valores realizáveis independentemente de autorização orçamentária e os valores numerários.
> § 2º O Ativo Permanente compreenderá os bens, créditos e valores, cuja mobilização ou alienação dependa de autorização legislativa.

Portanto, é preciso separar os ativos em financeiros e permanentes para calcular o superávit financeiro. Para isso, as contas contábeis têm um atributo chamado "indicador de superávit financeiro".

### Avaliação ISO 24495-1

| Princípio | Avaliação | Justificativa |
|---|---|---|
| Relevante | ✓ | O texto informa procedimentos contábeis obrigatórios para o setor público |
| Encontrável | ✓ | Títulos numéricos, bullet points no critério CEC, citações legais destacadas |
| Compreensível | ✓ | Frases quebradas, sequência de verbos substantivados desfeita, ordem direta |
| Utilizável/Acionável | ✓ | O contador sabe como classificar as contas após a leitura |

### Avisos finais

- **Órgão público:** a Lei 15.263/2025 obriga LS na administração pública. As 18 técnicas do art. 5º estão mapeadas no [`apêndice legal`](../../../.agents/skills/linguagem-simples-br/references/lei-15263-tecnicas.md).
- **Precisa de validação técnica externa:** texto contábil especializado. Um contador público deve validar antes de substituir o original.
- **Problema também é de processo:** o MCASP é denso porque a contabilidade pública é complexa — a simplificação melhora a legibilidade, mas não resolve a complexidade conceitual.

Fiz 5 mudanças. Quer a tabela antes/depois, a avaliação ISO detalhada ou a recomendação de teste com leitor?
