# Changelog

Este arquivo registra mudanças que afetam quem usa a skill. Métodos, entradas e resultados completos ficam em [`testes/resultados/`](testes/resultados/).

## v0.6.0-beta.4 — 06/10/26

### Adicionado

- Gerador reproduzível de pacotes para Claude web/Cowork, ChatGPT Skill e plugin do ChatGPT, todos derivados do mesmo `SKILL.md`.
- Variante Markdown do núcleo para Gemini web pessoal, gerada da fonte canônica sem manter uma segunda cópia editável.

### Corrigido

- Dados ausentes não podem virar datas, horários, valores ou links plausíveis nem em exemplos; a saída deve usar marcadores de confirmação.
- Contagens só podem aparecer depois de conferência mecânica.
- Rótulos gramaticais incertos devem ser omitidos em favor da descrição concreta da mudança.
- A avaliação de utilizabilidade agora exige ação, acesso e prazo completos no contexto fornecido e declara que análise técnica não prova compreensão.
- O inciso XI da Lei 15.263/2025 não pode justificar a retirada do masculino genérico.
- A descrição curta do Claude/Cowork ganhou gatilhos literais de revisão, simplificação e clareza.

### Verificado

- Os três ZIPs e a variante Markdown do Gemini passaram nas verificações locais de estrutura, integridade, versão e geração determinística.
- Claude web e Cowork passaram com Opus 5.5 em esforço médio; o núcleo do Gemini web passou com Flash 3.6.

### Ainda não verificado

- ChatGPT Skill e plugin do ChatGPT não foram enviados porque não havia conta elegível para o teste.

## v0.6.0-beta.3 — 30/09/26

### Corrigido

- Retirados textos jornalísticos e resultados derivados cuja licença subjacente não estava inequívoca para redistribuição.
- Removidos registros internos e referências a arquivos que não faziam parte do pacote público.
- A licença MIT passou a ser delimitada por `THIRD_PARTY_NOTICES.md` para não relicenciar textos-fonte de terceiros.
- README e skill agora descrevem de forma coerente o uso em textos de marca pessoal.
- Recomendações de design e teste deixaram de apresentar limites contextuais como regras universais.

### Verificado

- Os 10 arquivos foram instalados pela URL pública, conferidos byte a byte e carregados pelo OpenCode `1.18.33`.
- A Gabi instalou e usou a skill no Claude Code e no Codex; esses testes práticos ainda não têm roteiro reproduzível registrado.
- A árvore e o histórico público ficaram sem os materiais retirados, caminhos locais e registros internos excluídos.

## v0.6.0-beta.2 — 29/09/26

### Mudou

- A pergunta sobre revisar tudo ou só parte do texto aparece apenas quando existe uma escolha útil.
- Editais e atos normativos mantêm numeração, ordem e hierarquia. Quadros-resumo ficam separados do texto oficial.
- A barra de gênero, como em `candidato/a`, recebe tratamento próprio e não é confundida com flexão neutra.
- Demonstrativos sem referente claro são marcados para confirmação. A skill não completa a informação por conta própria.

### Verificado

- O edital T7 manteve itens e alíneas e foi reescrito sem pergunta de escopo desnecessária.
- O eval 11 manteve numeração, obrigação e prazo, retirou a barra e usou `[referente a confirmar]`.
- A instalação por `npx skills add` e o carregamento no OpenCode `1.18.33` foram reproduzidos.

Detalhes: [`testes/resultados/2026-09-29__ajuste-edital/`](testes/resultados/2026-09-29__ajuste-edital/).

## v0.6.0-beta.1 — 29/09/26

Primeira beta pública.

- Incluiu o pacote instalável, o apêndice da Lei 15.263/2025 e cinco exemplos com fonte.
- Corrigiu as travas de fidelidade, modalidade e citação literal.
- Separou a regra legal sobre flexão de gênero em órgãos públicos do tratamento dado a textos privados.
- Validou chamada explícita, descoberta automática, recursos locais e um fluxo completo no OpenCode `1.18.33`.

Detalhes: [`testes/resultados/2026-09-28__beta-comportamental/`](testes/resultados/2026-09-28__beta-comportamental/) e [`testes/resultados/2026-09-29__instalacao-beta/`](testes/resultados/2026-09-29__instalacao-beta/).

## Histórico anterior à publicação

- **v0.5.1 — 06/09/26:** subordinou o freio de sobre-edição à régua objetiva de frases longas.
- **v0.5 — 05/09/26:** acrescentou a trava de modalidade e o freio de sobre-edição.
- **v0.4 — 05/09/26:** reforçou fidelidade, delimitou Leitura Fácil e adotou entrega enxuta.
- **v0.3 — 24/05/26:** incorporou contexto regulatório, design da informação, teste com leitores e o apêndice legal.
- **v0.2 — 24/05/26:** melhorou planejamento, diagnóstico, preservação de voz e tratamento de textos longos.
- **v0.1 — 24/05/26:** primeira versão funcional.

## Limites atuais

- Ainda não houve teste com leitores do público-alvo.
- A instalação tem contraprova reproduzível no OpenCode. Claude Code e Codex passaram em testes práticos; nas demais ferramentas, a compatibilidade é esperada pelo formato Agent Skills, mas ainda não foi reproduzida.
- Cada caso comportamental teve uma execução por estado testado. Os resultados confirmam regressões específicas, não uma taxa geral de acerto.
