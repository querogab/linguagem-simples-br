# linguagem-simples-br

Skill para revisar textos em **Linguagem Simples** no português do Brasil.

Ela ajuda a encontrar problemas de estrutura, frases e vocabulário, reescreve o que atrapalha a leitura e inclui uma conferência para evitar a perda de fatos, prazos, condições e referências legais. Foi construída com base na **ABNT NBR ISO 24495-1:2024**, no [Manual de Linguagem Simples da Câmara dos Deputados](https://bd.camara.leg.br/bd/handle/bdcamara/41947) e na [Lei 15.263/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm).

> **Beta pública (`v0.6.0-beta.3`).** A instalação e a integridade do pacote foram verificadas de forma reproduzível no OpenCode `1.18.33`. A skill também foi instalada e usada com sucesso no Claude Code e no Codex. O teste com leitores do público-alvo continua pendente. Veja o [CHANGELOG](CHANGELOG.md).

## Veja um exemplo

**Antes**

> Contribuir para reduzir o tempo médio de titulação de mestres e doutores, a partir da capacitação de potenciais ingressantes em Programas de Pós-Graduação stricto sensu.

**Depois**

> Reduzir o tempo médio para formar mestres e doutores. Isso começa com a capacitação de quem pode ingressar em programas de pós-graduação stricto sensu.

A frase foi dividida e "potenciais ingressantes" virou "quem pode ingressar". Nenhum requisito de inscrição foi acrescentado. Este par veio de uma saída da v0.5.1 e foi conferido contra a [Chamada Pública nº 17/2025 da UECE](.agents/skills/linguagem-simples-br/exemplos/03-uece-objetivo.md). Ele mostra uma transformação pontual, não prova que todo o documento ficou mais fácil de entender.

## Para que serve

Use a skill para revisar:

- sites, e-mails, comunicados e FAQs;
- editais, ofícios e outros textos administrativos;
- materiais educativos e manuais;
- textos jurídicos ou técnicos dirigidos a quem não domina o assunto.

Ela também ajuda a escrever um texto novo, desde que você informe o público, o suporte e o que a pessoa precisa entender ou fazer.

A skill não substitui:

- uma segunda revisão de voz em texto de marca pessoal;
- validação jurídica, médica, financeira ou técnica;
- teste com leitores do público-alvo;
- diretrizes de **Leitura Fácil**, que exigem outro método e validação com pessoas com deficiência intelectual;
- revisão literária ou avaliação de linguagem neutra. Em texto de órgão público, ela apenas sinaliza a regra do inciso XI do art. 5º da Lei 15.263/2025.

## Como instalar

O pacote segue o formato [Agent Skills](https://agentskills.io/) e está em [`.agents/skills/linguagem-simples-br/`](.agents/skills/linguagem-simples-br/).

### Pelo terminal

```bash
npx skills add querogab/linguagem-simples-br
```

O instalador identifica as ferramentas disponíveis e instala no projeto atual. Para disponibilizar a skill em todos os projetos, use:

```bash
npx skills add querogab/linguagem-simples-br -g
```

### Sem terminal

1. Neste repositório, clique em **Code > Download ZIP** e descompacte o arquivo.
2. Localize `.agents/skills/linguagem-simples-br/` e copie a pasta inteira, sem retirar `LICENSE`, `THIRD_PARTY_NOTICES.md`, `references/` ou `exemplos/`.
3. Use a pasta de skills da sua ferramenta:
   - OpenCode: `.opencode/skills/`
   - Claude Code: `.claude/skills/` no projeto ou `~/.claude/skills/` para uso global
   - Codex: `.agents/skills/` no projeto ou `~/.agents/skills/` para uso global
4. Se a skill não aparecer, feche e abra a ferramenta.

Em uma ferramenta que não carrega Agent Skills, você pode colar o conteúdo do `SKILL.md`, sem o cabeçalho entre `---`, no campo de instruções. Nesse modo, os arquivos de `references/` e `exemplos/` não ficam disponíveis automaticamente. O uso manual ainda não foi testado nesta beta.

## Como usar

Peça a revisão diretamente:

```text
Revise este texto em linguagem simples:
[cole o texto]
```

Ou chame a skill pelo nome:

```text
Use a skill linguagem-simples-br para revisar este texto:
[cole o texto]
```

Depois de acionada, ela:

1. identifica se o texto é público ou privado e lê o contexto disponível;
2. pergunta apenas o que não conseguiu inferir sobre público, suporte e objetivo;
3. diagnostica burocratês, arquitetura da informação, frases e palavras;
4. decide o que deve permanecer intacto antes de reescrever;
5. confere fatos, itens, prazos, valores, condições, modalidade e referências legais;
6. entrega a versão final e os avisos necessários.

Por padrão, a resposta é curta. A tabela antes/depois, a avaliação pelos quatro princípios da ISO 24495-1 e a recomendação de teste aparecem quando você pede, quando o texto é de órgão público ou quando ativa o modo didático.

Para aprender durante a revisão, use um destes pedidos:

```text
Me ensina os 3 principais.
Me ensina tudo.
Me ensina sobre [diretriz].
```

## O que diferencia esta skill

### Feita para o contexto brasileiro

A skill reúne a norma brasileira de Linguagem Simples, o Manual da Câmara e a Lei 15.263/2025. Para textos de órgão público, o apêndice [`lei-15263-tecnicas.md`](.agents/skills/linguagem-simples-br/references/lei-15263-tecnicas.md) organiza as 18 técnicas do art. 5º como checklist e registra os limites dos arts. 6º, 7º e 8º.

### Preserva o grau de certeza

Simplificar não autoriza trocar possibilidade por certeza. A skill trata palavras como "poderá", "deverá", "pretende", "até" e "aproximadamente" como parte do conteúdo. Também confere listas, prazos, exceções e remissões legais antes de entregar.

### Evita mudanças sem ganho de clareza

O fluxo manda identificar primeiro o que já está claro. A intenção é reduzir mudanças cosméticas, que gastam tempo de revisão e abrem espaço para perda de informação. O mecanismo existe, mas ainda precisa de nova avaliação pública com material redistribuível que misture frases curtas e longas.

### Separa Linguagem Simples de Leitura Fácil

Se o pedido for de Leitura Fácil, a skill explica a diferença e oferece apenas um rascunho para validação. Material de Leitura Fácil precisa ser validado por pessoas com deficiência intelectual; uma IA ou uma pessoa redatora não consegue declarar o texto pronto sozinha. Esse foi o único comportamento em que o modelo sem a skill falhou nos dois modelos testados.

### Trata teste com leitores como parte do trabalho

A avaliação automática é só um indício. A skill recomenda leitura em voz alta, pergunta de compreensão, teste de lacunas ou observação de uso, conforme o texto e a ação esperada.

## O que foi medido

Cinco gêneros de texto público foram revisados em três condições: modelo sem instrução adicional, prompt curto de oito linhas e skill. Cada condição rodou uma vez, no mesmo modelo e em uma janela separada.

| Medida | Modelo sozinho | Prompt de 8 linhas | Com a skill |
|---|---:|---:|---:|
| Média de frases acima de 30 palavras nos cinco textos | 11,8% | **0,0%** | 3,3% |
| Itens preservados no art. 5º da Lei 15.263 | 18/18 | 18/18 | 18/18 |
| Itens preservados no art. 46 da Lei 9.610 | 11/11 | 11/11 | 11/11 |

O resultado é direto: para encurtar frases, o prompt de oito linhas foi melhor. Na cobertura dos dois textos legais, houve empate. A skill não alega superioridade nesses pontos.

As medidas de tamanho são **proxies de legibilidade**, não prova de compreensão. Os números vêm da v0.5.1 e não são atribuídos automaticamente à beta atual. Uma execução por condição também não permite estimar variação entre rodadas.

O que a execução da v0.5.1 demonstrou:

- a skill reduziu a proporção de frases longas em relação ao modelo sozinho;
- preservou todos os itens contados nos dois textos legais;
- recusou tratar um rascunho como Leitura Fácil pronta e explicou a validação necessária.

Nas contraprovas da beta, a skill preservou citação, numeração, modalidade e prazo e marcou um referente ausente sem inventar a informação.

O [plano de testes](testes/plano-de-testes.md), o [critério de cobertura](testes/gabarito-cobertura.md), o [`medir.py`](testes/medir.py) e os [resultados](testes/resultados/) estão publicados. Resultados afetados por vazamento de contexto ou por material sem redistribuição inequívoca não sustentam as alegações desta página.

## Limites atuais

- Ainda não houve teste com leitores do público-alvo.
- Claude Code e Codex funcionaram em testes práticos, mas ainda não têm uma contraprova reproduzível registrada como a do OpenCode.
- Compatibilidade com outras ferramentas é esperada quando elas implementam Agent Skills, mas não está garantida.
- Os cinco pares em [`exemplos/`](.agents/skills/linguagem-simples-br/exemplos/README.md) vieram da v0.5.1. Eles foram conferidos, mas não reexecutados na beta.
- A skill foi construída contra a parte 1 da ISO 24495. As partes setoriais para comunicação jurídica e científica estão fora do escopo atual.
- Nenhuma métrica automática substitui a leitura por pessoas do público real.

## Próximos passos

A v1.0 depende de uso externo, teste com pelo menos uma pessoa do público-alvo e fechamento da documentação. O histórico das versões está no [CHANGELOG](CHANGELOG.md).

## Licença

O código, a skill e a documentação autoral estão sob **MIT**. Trechos de documentos-fonte e o controle da Agência Senado não são relicenciados pela MIT. As origens, os limites e as autorizações aplicáveis estão em [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Contribuições

Abra uma issue com um caso de uso, uma dúvida ou um problema encontrado. Texto que deu errado na revisão é a contribuição mais útil: ele mostra onde a regra precisa melhorar.

## Créditos

- **Patricia Roedel**, autora do Manual de Linguagem Simples da Câmara dos Deputados
- **Heloísa Fischer**, pioneira de Linguagem Simples no Brasil e fundadora da [Comunica Simples](https://comunicasimples.com.br)
- **ICICT/Fiocruz**, Guia de Linguagem e Design Simples
- **International Plain Language Federation**, [definição internacional de Plain Language](https://www.iplfederation.org/plain-language/)
