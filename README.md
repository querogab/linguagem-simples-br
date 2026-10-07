# linguagem-simples-br

**Linguagem Simples** é uma forma de comunicar que organiza palavras, estrutura e design para ajudar o público a encontrar, entender e usar a informação de que precisa.

Esta é uma skill para revisar textos em **Linguagem Simples** no português do Brasil. Uma skill é um pacote de instruções que ensina um assistente de IA, como o Claude ou o Gemini, a fazer uma tarefa.

Ela ajuda a encontrar problemas de estrutura, frases e vocabulário e reescreve o que atrapalha a leitura. Também faz uma conferência para evitar que fatos, prazos, condições e referências legais se percam. Foi construída com base na **ABNT NBR ISO 24495-1:2024**, no [Manual de Linguagem Simples da Câmara dos Deputados](https://bd.camara.leg.br/bd/handle/bdcamara/41947) e na [Lei 15.263/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm).

> **Beta pública (`v0.6.0-beta.4`).** É uma versão de teste aberta a qualquer pessoa. Ela já funciona, mas ainda pode mudar e tem limites conhecidos, listados em [Limites atuais](#limites-atuais).
>
> O que foi testado nesta versão:
>
> - **Claude web e Cowork:** a skill passou num teste curto, com uma frase de exemplo.
> - **Gemini web:** uma versão reduzida, sem os arquivos de apoio, passou no mesmo teste.
> - **OpenCode `1.18.33`:** um roteiro que pode ser repetido confirmou que a instalação funciona e que os arquivos chegam completos e iguais aos originais.
> - **Claude Code e Codex:** a skill foi instalada e usada com sucesso, mas sem roteiro registrado.
>
> Ainda faltam o teste com leitores do público-alvo e os testes de uso no ChatGPT e no Copilot. Se você testar a skill, conte como foi no [formulário de retorno](https://forms.gle/mEHuUrvx5aYQMhus7). O histórico das versões está no [CHANGELOG](CHANGELOG.md).

## Veja um exemplo

**Antes**

> O parâmetro para que uma aplicação financeira possa ser enquadrada como CEC é que: possua a finalidade de atender a compromissos de caixa de curto prazo e não investimento ou outros fins, seja prontamente conversível em quantia conhecida de caixa, no curto prazo e esteja sujeita a risco insignificante de mudança de valor.

**Depois**

> Para que uma aplicação financeira seja classificada como equivalente de caixa (CEC), ela precisa:
>
> - ter a finalidade de atender a compromissos de caixa de curto prazo (e não investimento ou outros fins)
> - ser prontamente conversível em uma quantia conhecida de caixa, no curto prazo
> - estar sujeita a risco insignificante de mudança de valor

A sigla foi expandida e os três critérios ficaram separados. Nenhuma condição foi retirada. Este par foi produzido pela v0.5.1 da skill e conferido com o [Manual de Contabilidade Aplicada ao Setor Público](.agents/skills/linguagem-simples-br/exemplos/02-mcasp-aplicacoes.md). Ele mostra uma transformação pontual e não dispensa validação técnica do conteúdo contábil.

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

Escolha o caminho pela ferramenta que você usa. Se você usa o assistente de IA pelo navegador, comece por [Interfaces web](#interfaces-web). Esse caminho não exige terminal.

### Interfaces web

Baixe o arquivo da sua ferramenta na [página desta versão (release `v0.6.0-beta.4`)](https://github.com/querogab/linguagem-simples-br/releases/tag/v0.6.0-beta.4).

#### Claude web e Cowork

[Baixe o ZIP para Claude web e Cowork](https://github.com/querogab/linguagem-simples-br/releases/download/v0.6.0-beta.4/linguagem-simples-br-claude-web-cowork-0.6.0-beta.4.zip). Depois, em **Customize > Skills**, escolha **Upload a skill** e envie o arquivo baixado. A [Anthropic documenta](https://support.claude.com/en/articles/12512180-use-skills-in-claude) o recurso nos planos Free, Pro, Max, Team e Enterprise e o uso da mesma skill no chat e no Cowork. A opção de executar código precisa estar ativada. Organizações podem restringir o envio de skills.

#### Gemini web

[Baixe o `SKILL.md` para Gemini web](https://github.com/querogab/linguagem-simples-br/releases/download/v0.6.0-beta.4/SKILL.md). Em uma conta pessoal com Skills liberadas, abra **Skills** e envie o arquivo baixado. Esta versão troca somente três instruções que o Gemini Flash interpretou de forma diferente nos testes. A interface observada em 06/10/26 aceitou Markdown, mas não ZIP. Os arquivos de apoio, `references/` e `exemplos/`, não vão junto. Esta opção instala só o núcleo da revisão. O recurso está em implantação gradual e pode ainda não aparecer em todas as contas. Veja a [documentação do Gemini Apps](https://support.google.com/gemini/answer/17094296).

#### GitHub Copilot

O Copilot no VS Code, o Copilot CLI e o cloud agent no GitHub usam a pasta canônica completa, com referências e exemplos. O comando `gh skill` está em preview e exige GitHub CLI 2.90.0 ou posterior.

Para instalar no VS Code e no CLI, disponível em todos os projetos locais:

```bash
gh skill install querogab/linguagem-simples-br linguagem-simples-br@v0.6.0-beta.4 --allow-hidden-dirs --agent github-copilot --scope user
```

Para usar no Copilot web/cloud agent, execute no repositório em que ele vai trabalhar:

```bash
gh skill install querogab/linguagem-simples-br linguagem-simples-br@v0.6.0-beta.4 --allow-hidden-dirs --agent github-copilot --scope project
git add .agents/skills/linguagem-simples-br
```

Depois, versione a pasta junto do projeto. O Copilot web não oferece upload pessoal de skill; ele lê a skill que está no repositório da tarefa. A estrutura foi validada e visualizada pelo `gh skill`, mas o comportamento ainda não foi testado numa conta do Copilot.

#### ChatGPT web

[Baixe o ZIP para ChatGPT](https://github.com/querogab/linguagem-simples-br/releases/download/v0.6.0-beta.4/linguagem-simples-br-chatgpt-skill-0.6.0-beta.4.zip). Em uma [conta elegível](https://help.openai.com/articles/20001066) do ChatGPT Business, Enterprise, Healthcare ou Edu, abra **Plugins > Skills > Create > Upload from your computer** e envie o arquivo baixado.

Há também um [ZIP de plugin para distribuição](https://github.com/querogab/linguagem-simples-br/releases/download/v0.6.0-beta.4/linguagem-simples-br-chatgpt-plugin-0.6.0-beta.4.zip). Ele não é necessário para instalar a skill. Publicá-lo no diretório da OpenAI exige o [processo próprio de submissão e revisão](https://developers.openai.com/plugins/deploy/submission).

Claude web, Cowork e o núcleo do Gemini web passaram no reteste da beta.4. ChatGPT web ainda não foi testado por falta de conta elegível.

Quem mantém o projeto pode recriar esses arquivos a partir da fonte canônica com `python scripts/gerar-pacotes-web.py`. O script confere a estrutura, a integridade e a versão de cada arquivo antes de gravá-lo.

### Pelo terminal

```bash
npx skills add querogab/linguagem-simples-br
```

O instalador identifica as ferramentas disponíveis e instala no projeto atual. Para disponibilizar a skill em todos os projetos, use:

```bash
npx skills add querogab/linguagem-simples-br -g
```

### Copiando a pasta

Este caminho serve para OpenCode, Claude Code e Codex, sem usar o terminal. A skill segue o formato [Agent Skills](https://agentskills.io/) e está em [`.agents/skills/linguagem-simples-br/`](.agents/skills/linguagem-simples-br/).

1. Neste repositório, clique em **Code > Download ZIP** e descompacte o arquivo.
2. Localize `.agents/skills/linguagem-simples-br/` e copie a pasta inteira, sem retirar `LICENSE`, `THIRD_PARTY_NOTICES.md`, `references/` ou `exemplos/`.
3. Use a pasta de skills da sua ferramenta:
   - OpenCode: `.opencode/skills/`
   - Claude Code: `.claude/skills/` no projeto ou `~/.claude/skills/` para uso global
   - Codex: `.agents/skills/` no projeto ou `~/.agents/skills/` para uso global
4. Se a skill não aparecer, feche e abra a ferramenta.

### Em outras ferramentas

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

1. identifica se o texto é de órgão público ou privado e lê o contexto disponível;
2. pergunta apenas o que não conseguiu inferir sobre público, suporte e objetivo;
3. aponta burocratês e problemas de organização, frases e palavras;
4. decide o que deve permanecer intacto antes de reescrever;
5. confere fatos, itens, prazos, valores, condições, grau de certeza e referências legais;
6. entrega a versão final e os avisos necessários.

Por padrão, a resposta é curta. Três partes só aparecem em alguns casos: a tabela antes/depois, a avaliação pelos quatro princípios da ISO 24495-1 e a recomendação de teste com leitores. Elas aparecem quando você pede, quando o texto é de órgão público ou quando você ativa o modo didático.

Para ativar o modo didático e aprender durante a revisão, use um destes pedidos:

```text
Me ensina os 3 principais.
Me ensina tudo.
Me ensina sobre [diretriz].
```

## O que diferencia esta skill

### Feita para o contexto brasileiro

A skill reúne a norma brasileira de Linguagem Simples, o Manual da Câmara e a Lei 15.263/2025. Para textos de órgão público, o apêndice [`lei-15263-tecnicas.md`](.agents/skills/linguagem-simples-br/references/lei-15263-tecnicas.md) organiza as 18 técnicas do art. 5º como checklist. Ele também explica os arts. 6º, 7º e 8º.

### Preserva o grau de certeza

Simplificar não autoriza trocar possibilidade por certeza. A skill trata palavras como "poderá", "deverá", "pretende", "até" e "aproximadamente" como parte do conteúdo. Também confere listas, prazos, exceções e remissões legais antes de entregar.

### Evita mudanças sem ganho de clareza

O fluxo manda identificar primeiro o que já está claro. A intenção é reduzir mudanças cosméticas, que gastam tempo de revisão e abrem espaço para perda de informação. O mecanismo existe, mas ainda precisa de uma nova avaliação aberta, feita com textos que possam ser publicados e que misturem frases curtas e longas.

### Separa Linguagem Simples de Leitura Fácil

Se o pedido for de Leitura Fácil, a skill explica a diferença e oferece apenas um rascunho para validação. Material de Leitura Fácil precisa ser validado por pessoas com deficiência intelectual; uma IA ou uma pessoa redatora não consegue declarar o texto pronto sozinha. Foi o único comportamento em que os dois modelos testados falharam sem a skill.

### Trata teste com leitores como parte do trabalho

A avaliação automática é só um indício. A skill recomenda leitura em voz alta, pergunta de compreensão, teste de lacunas ou observação de uso, conforme o texto e a ação esperada.

## O que os testes mostraram

Os testes fizeram perguntas diferentes. A primeira foi: **qual instrução produz menos frases longas?** A segunda: **qual delas preserva todos os itens de um texto legal?** Separar as duas evita tratar frase curta como sinônimo de texto fiel ou fácil de entender.

Na v0.5.1, cinco gêneros de texto de órgão público foram revisados de três formas:

1. só o modelo, sem instrução adicional;
2. o modelo com um prompt de oito linhas;
3. o modelo com a skill.

Cada forma rodou uma vez por texto, sempre no modelo `deepseek-v4-flash` e em uma conversa separada. Com outro modelo, os números podem ser diferentes.

Como o resultado de um prompt depende do que ele pede, o prompt de oito linhas vai transcrito aqui:

> Reescreva em português claro. Frases de até 20 palavras. Voz ativa. Uma ideia por frase. Troque substantivo abstrato por verbo. Não perca nenhum fato, prazo ou condição. Diga a quem a regra se aplica. Não infantilize.

São oito instruções curtas de escrita clara, e uma delas manda preservar fatos, prazos e condições. O prompt não traz exemplos nem pede diagnóstico ou conferência antes da entrega. O mesmo texto está no [plano de testes](testes/plano-de-testes.md).

### 1. Qual produziu menos frases longas?

| Forma de revisão | Média de frases acima de 30 palavras |
|---|---:|
| Só o modelo | 11,8% |
| Prompt de 8 linhas | **0,0%** |
| Com a skill | 3,3% |

O prompt de oito linhas foi o melhor para encurtar frases: não deixou nenhuma acima de 30 palavras. A skill ficou entre ele e o modelo sozinho.

Esse número mede apenas o tamanho das frases. Frase curta pode continuar confusa ou perder informação. Só um teste com leitores mostra se o público encontra, entende e usa o conteúdo.

### 2. Qual preservou os itens dos textos legais?

As três formas empataram nos dois textos usados para essa conferência:

- art. 5º da Lei 15.263: **18 de 18 itens preservados**;
- art. 46 da Lei 9.610: **11 de 11 itens preservados**.

O teste mostra que a skill preservou todos os itens contados nesses dois textos. Não mostra que ela preservará todo fato em qualquer documento, nem que supera um prompt curto nessa tarefa.

### 3. O que foi conferido na beta?

Na beta, testes específicos conferiram se problemas encontrados no uso tinham sido corrigidos. Nesses testes, a skill:

- manteve uma citação literal;
- preservou numeração, grau de certeza e prazo;
- marcou a dúvida quando não dava para saber a que uma palavra se referia, em vez de inventar a resposta.

Em outro teste de escopo, a skill recusou apresentar um rascunho como Leitura Fácil pronta e explicou a validação necessária. Sem a skill, os dois modelos testados falharam nesse ponto.

### Como interpretar

Se o único objetivo é encurtar frases, o prompt de oito linhas foi suficiente e teve o melhor resultado. A skill acrescenta um fluxo que diagnostica o texto, confere o resultado e trata casos como Leitura Fácil, grau de certeza e contexto legal brasileiro. Os testes ainda não permitem afirmar que ela melhora a compreensão do público.

Os números vêm da v0.5.1 e não são atribuídos automaticamente à beta atual. Como cada condição rodou uma vez, também não há uma taxa geral de acerto nem uma estimativa de variação entre rodadas.

O [plano de testes](testes/plano-de-testes.md), o [critério de cobertura](testes/gabarito-cobertura.md), o [`medir.py`](testes/medir.py) e os [resultados](testes/resultados/) estão publicados. As conclusões acima usam apenas testes em que cada forma de revisão rodou separada das outras, com materiais que podiam ser publicados. Ficaram de fora os resultados em que o modelo já tinha visto a skill antes do teste. Também ficaram de fora os que usaram textos sem permissão clara de redistribuição.

## Limites atuais

- Ainda não houve teste com leitores do público-alvo.
- Claude Code e Codex funcionaram em testes práticos, mas ainda não têm um roteiro de teste que possa ser repetido, como o do OpenCode.
- O ChatGPT web e o GitHub Copilot ainda não foram testados no uso.
- Compatibilidade com outras ferramentas é esperada quando elas implementam Agent Skills, mas não está garantida.
- Os cinco pares em [`exemplos/`](.agents/skills/linguagem-simples-br/exemplos/README.md) vieram da v0.5.1. Eles foram conferidos, mas não reexecutados na beta.
- A skill foi construída com base na parte 1 da ISO 24495. As partes da norma voltadas à comunicação jurídica e científica estão fora do escopo atual.
- Nenhuma métrica automática substitui a leitura por pessoas do público real.

## Próximos passos

A versão 1.0 depende de uso por pessoas de fora do projeto, de teste com pelo menos uma pessoa do público-alvo e da documentação concluída. O histórico das versões está no [CHANGELOG](CHANGELOG.md).

## Licença

O código, a skill e a documentação escrita para este projeto estão sob a licença **MIT**. A MIT não vale para os trechos de documentos-fonte nem para a notícia da Agência Senado usada como texto de controle nos testes. A origem de cada um, os limites de uso e as autorizações estão em [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Contribuições

Testou a skill? Conte como foi no [formulário de retorno](https://forms.gle/mEHuUrvx5aYQMhus7). Não é preciso ter conta no GitHub. Quem tem conta também pode abrir uma issue, que é um relato público no GitHub. Ela serve para contar um caso de uso, uma dúvida ou um problema encontrado.

Texto que deu errado na revisão é a contribuição mais útil: ele mostra onde a regra precisa melhorar. Não envie texto sigiloso nem dados pessoais de outras pessoas.

## Referências

A fundamentação da skill e os links para as obras consultadas estão na seção [Referências do `SKILL.md`](.agents/skills/linguagem-simples-br/SKILL.md#referências). A presença nessa lista indica fonte de consulta, não participação das autoras ou instituições no desenvolvimento deste projeto.
