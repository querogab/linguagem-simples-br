---

**Original:** T6__manual-mcasp.txt
**Condição:** skill (v0.4)
**Modelo:** deepseek-v4-flash

---

## PASSO 2 — DIAGNÓSTICO RÁPIDO

**A) Sinais de burocratês**

| # | Achado | Exemplo |
|---|--------|---------|
| 1 | Nariz de cera | — |
| 2 | Privilegiar quem faz | "destacamos" — quem? |
| 3 | Base legal antes do conteúdo | A Lei 4.320/64 é citada antes de explicar o conceito |
| 4 | Propagandear processo interno | — |
| 5 | Verbos substantivados | classificação, restrições, finalidade, mensuração, rendimentos, segregação, apuração |
| 6 | Jargão sem explicação | CEC, superavit financeiro, custo amortizado, valor justo, pré-fixadas/pós-fixadas |
| 7 | Sigla sem expansão | CEC (nunca expandida no texto) |
| 8 | Maiúsculas desnecessárias | Disponibilidades, Balanço, Ativo Circulante, Realizável a Longo Prazo |

**B) Arquitetura**

- Primeiro parágrafo começa no meio de uma frase — falta contexto
- Info importante (definição de superavit financeiro) enterrada em citação legal
- Mais de uma ideia por parágrafo (ex.: primeiro parágrafo mistura regra de depósito com classificação contábil)
- Falta de estrutura escaneável: texto denso sem separação visual

**C) Frases**

- "O parâmetro para que uma aplicação financeira possa ser enquadrada como CEC é que: possua a finalidade de atender a compromissos de caixa de curto prazo e não investimento ou outros fins, seja prontamente conversível em quantia conhecida de caixa, no curto prazo e esteja sujeita a risco insignificante de mudança de valor." — **47 palavras**, uma só frase
- Voz passiva: "são classificáveis", "deve ser utilizado", "estão expostos"
- Ordem inversa: "Quanto ao requisito de risco insignificante..."

**D) Palavras**

- Verbos substantivados: classificação, mensuração, rendimentos, segregação, apuração, mobilização
- Palavras raras: prontamente conversível, volatilidade, enquadramento, mobilização
- Estrangeirismos: —

---

## PASSO 3 — HEURÍSTICA

Texto com ~400 palavras (entre 301 e 1000). Como a instrução do usuário foi "revisa este texto", a reescrita será integral.

---

## PASSO 4 — REESCRITA

### Tabela antes/depois/por quê

| Antes | Depois | Por quê |
|-------|--------|---------|
| "tais Depósitos Bancários Vinculados não devem integrar o saldo das Disponibilidades, e sua classificação no Balanço deve levar em conta suas características específicas" | Depósitos bancários vinculados são valores com destinação específica. Eles **não** entram no saldo de disponibilidades (dinheiro disponível). | Voz ativa. "Disponibilidades" vira explicação entre parênteses. Uma ideia por frase. |
| "são classificáveis em conta à parte no Ativo Circulante ou Realizável a Longo Prazo, na condição de créditos e valores a receber" | No balanço, eles ficam em conta separada, como créditos a receber — no curto prazo (Ativo Circulante) ou no longo prazo. | "Classificáveis" vira "ficam". Siglas explicadas. Ordem direta. |
| "O parâmetro para que uma aplicação financeira possa ser enquadrada como CEC é que: possua a finalidade de atender a compromissos de caixa de curto prazo e não investimento ou outros fins, seja prontamente conversível em quantia conhecida de caixa, no curto prazo e esteja sujeita a risco insignificante de mudança de valor" | Para ser classificada como CEC (Caixa e Equivalentes de Caixa), a aplicação financeira precisa: • servir para pagar compromissos de curto prazo (não para investimento) • poder virar dinheiro rápido, em valor conhecido • ter risco muito baixo de mudança de valor | Frase de 47 palavras quebrada em 3 itens + cabeçalho. CEC expandido. "Finalidade" vira "servir para". |
| "classificar as aplicações financeiras em pré-fixadas ou pós-fixadas não é um critério que deve ser utilizado para definir o nível de risco, uma vez que os dois tipos de investimentos estão expostos à volatilidade do mercado, assim, realizar tal distinção, não determina o enquadramento das aplicações quanto à mensuração, se custo amortizado ou valor justo" | Para avaliar o risco, não basta separar as aplicações entre pré-fixadas (taxa fixa) e pós-fixadas (taxa variável). Os dois tipos sofrem oscilações do mercado. Por isso, essa diferença não define se a aplicação deve ser medida pelo custo amortizado ou pelo valor justo. | Três frases no lugar de uma. Termos explicados entre parênteses. "Utilizado" vira "basta". "Volatilidade" vira "oscilações". |
| "Nesse contexto destacamos os artigos 43 e 105 da referida norma" | Veja o que diz a lei: | Corte do "nós" institucional. Linguagem direta. |
| "é necessário segregar os ativos em: financeiros e permanentes, para fins de apuração do superavit financeiro e para tanto as contas contábeis possuem um atributo de indicador de superavit financeiro" | Por isso, as contas contábeis têm um indicador que classifica cada ativo como financeiro ou permanente. Essa separação é necessária para calcular o superavit financeiro. | Duas frases no lugar de uma. Ordem direta. |

---

### Versão final limpa

**Depósitos bancários vinculados**

Depósitos bancários vinculados são valores que têm uma destinação específica. Eles **não** entram no saldo de disponibilidades (dinheiro disponível). No balanço, eles ficam em uma conta separada, como créditos a receber — no curto prazo (Ativo Circulante) ou no longo prazo.

**4.3.3 Aplicações Financeiras**

Para ser classificada como CEC (Caixa e Equivalentes de Caixa), a aplicação financeira precisa:

- servir para pagar compromissos de curto prazo (e não para investimento ou outros fins)
- poder ser convertida em dinheiro rapidamente, em valor conhecido
- ter risco muito baixo de mudança de valor

Para avaliar o risco, não basta separar as aplicações entre pré-fixadas (taxa fixa) e pós-fixadas (taxa variável). Os dois tipos sofrem oscilações do mercado. Por isso, essa diferença não define se a aplicação deve ser medida pelo custo amortizado ou pelo valor justo.

Os rendimentos das aplicações de liquidez imediata (que são equivalentes de caixa) acompanham o valor principal. Eles devem ser registrados junto com o saldo disponível, no grupo CEC.

**4.4 Aspectos Orçamentários**

Para calcular o superavit financeiro (sobra de recursos), a Lei nº 4.320/64 exige separar os ativos em dois grupos: financeiros e permanentes. O superavit financeiro serve como fonte para abrir créditos adicionais.

Veja o que diz a lei:

- **Art. 43, § 2º:** Superavit financeiro é a diferença positiva entre o ativo financeiro e o passivo financeiro, considerando também os saldos de créditos adicionais transferidos e as operações de crédito vinculadas.
- **Art. 105, § 1º:** O Ativo Financeiro inclui os créditos e valores que podem ser realizados sem autorização orçamentária, além dos valores em dinheiro.
- **Art. 105, § 2º:** O Ativo Permanente inclui os bens, créditos e valores que dependem de autorização legislativa para serem vendidos ou transferidos.

Por isso, as contas contábeis têm um indicador que classifica cada ativo como financeiro ou permanente. Essa separação é necessária para calcular o superavit financeiro.

---

### Avaliação ISO 24495-1:2024

| Princípio | ✓/✗/N/A | Justificativa |
|-----------|----------|---------------|
| **Relevância** | ✓ | Mantém todos os conceitos necessários (CEC, superavit, classificação de ativos). |
| **Localizabilidade** | ✓ | Estrutura com subtítulos e lista de itens permite varredura visual. |
| **Compreensibilidade** | ✓ | Siglas expandidas, jargão explicado entre parênteses, frases reduzidas para 15-20 palavras. |
| **Usabilidade** | ✓ | Cidadão consegue identificar rapidamente o que é CEC, o que são depósitos vinculados e como funciona o superavit. |

---

### Avisos finais

1. **Validação técnica necessária:** Esta versão foi adaptada para o cidadão comum. Recomenda-se revisão por contador público antes da publicação oficial.
2. **Trava de fidelidade respeitada:** Todos os artigos de lei (Art. 43, § 2º; Art. 105, § 1º e § 2º; Lei nº 4.320/64), prazos e conceitos contábeis foram preservados.
3. **Lei 15.263/2025:** Esta adaptação está em conformidade com o direito do cidadão à comunicação clara em serviços públicos. O texto original em jargão técnico deve permanecer disponível como referência.
4. **Teste com leitor real:** Recomenda-se testar esta versão com 3 a 5 cidadãos sem formação em contabilidade antes da implementação.