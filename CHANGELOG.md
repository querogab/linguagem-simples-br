# Changelog

Este arquivo registra mudanças que afetam quem usa a skill. Cada caso foi testado uma vez por versão, então os resultados confirmam correções específicas, não uma taxa de acerto. Resultados completos em [`testes/resultados/`](testes/resultados/); limites atuais no [README](README.md#limites-atuais).

## Em desenvolvimento

### Mudou

- README revisado com a própria skill, com instruções para o GitHub Copilot e links diretos para baixar os arquivos das interfaces web.
- [Formulário de retorno](https://forms.gle/mEHuUrvx5aYQMhus7) que não exige conta no GitHub.

## v0.6.0-beta.4 — 06/10/26

### Mudou

- Arquivos para instalar pelo navegador no Claude web, no Cowork, no Gemini web e no ChatGPT.
- Dado ausente, como data, horário, valor ou link, vira um marcador como `[data a confirmar]`, nunca um valor inventado.
- Contagens só aparecem depois de conferidas, e rótulos gramaticais incertos dão lugar à descrição da mudança.
- O texto só é avaliado como utilizável com ação, acesso e prazo completos. A avaliação avisa que análise técnica não prova compreensão.
- A skill não usa mais o inciso XI da Lei 15.263/2025 para justificar a retirada do masculino genérico.
- No Cowork, a skill passou a ser acionada também quando o pedido não cita o nome dela.

### Verificado

- Claude web e Cowork passaram com Opus 5.5 em esforço médio, num teste curto com uma frase de exemplo.
- A versão reduzida para o Gemini web passou no mesmo teste com Flash 3.6.
- O ChatGPT não foi testado por falta de conta elegível.

## v0.6.0-beta.3 — 30/09/26

### Mudou

- Saíram textos e resultados sem licença clara de redistribuição, e a MIT deixou de cobrir textos-fonte de terceiros ([`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)).
- README e skill passaram a orientar do mesmo jeito o uso em textos de marca pessoal.
- Recomendações de design e de teste deixaram de apresentar limites de um contexto como regras universais.

### Verificado

- A skill foi instalada pela URL pública e carregada no OpenCode `1.18.33`, com os 10 arquivos conferidos byte a byte.
- A skill também foi instalada e usada no Claude Code e no Codex, ainda sem roteiro de teste registrado.

## v0.6.0-beta.2 — 29/09/26

### Mudou

- A pergunta sobre revisar tudo ou só parte do texto aparece apenas quando existe uma escolha útil.
- Editais e atos normativos mantêm numeração, ordem e hierarquia. Quadros-resumo ficam separados do texto oficial.
- A barra de gênero, como em `candidato/a`, recebe tratamento próprio e não é confundida com flexão neutra.
- Palavras como "este" ou "esses", quando não se sabe a que se referem, ficam marcadas para confirmação, sem completar a informação.

### Verificado

- Num edital real, a skill manteve itens e alíneas e não fez pergunta de escopo desnecessária.
- Num caso de teste, a skill manteve numeração, obrigação e prazo, retirou a barra de gênero e usou `[referente a confirmar]`.
- A instalação por `npx skills add` e o carregamento no OpenCode `1.18.33` foram reproduzidos.

Detalhes: [`testes/resultados/2026-09-29__ajuste-edital/`](testes/resultados/2026-09-29__ajuste-edital/).

## v0.6.0-beta.1 — 29/09/26

Primeira beta pública.

### Mudou

- Inclui o pacote instalável, o apêndice da Lei 15.263/2025 e cinco exemplos com fonte.
- As travas de fidelidade, de grau de certeza e de citação literal foram corrigidas.
- A regra legal sobre flexão de gênero em órgãos públicos ficou separada do tratamento dado a textos privados.

### Verificado

- No OpenCode `1.18.33`, funcionaram a chamada pelo nome, o acionamento automático, o acesso aos arquivos de apoio e um fluxo completo.

Detalhes: [`testes/resultados/2026-09-28__beta-comportamental/`](testes/resultados/2026-09-28__beta-comportamental/) e [`testes/resultados/2026-09-29__instalacao-beta/`](testes/resultados/2026-09-29__instalacao-beta/).

## Histórico anterior à publicação

- **v0.5.1 — 06/09/26:** frases acima de 30 palavras e outras construções condenadas pela régua da skill passaram a ser corrigidas mesmo quando pareciam claras.
- **v0.5 — 05/09/26:** a skill passou a preservar o grau de certeza do original e a evitar mudanças sem ganho de clareza.
- **v0.4 — 05/09/26:** reforçou a fidelidade ao original, separou Linguagem Simples de Leitura Fácil e passou a entregar respostas curtas por padrão.
- **v0.3 — 24/05/26:** incorporou contexto regulatório, design da informação, teste com leitores e o apêndice legal.
- **v0.2 — 24/05/26:** melhorou planejamento, diagnóstico, preservação de voz e tratamento de textos longos.
- **v0.1 — 24/05/26:** primeira versão funcional.
