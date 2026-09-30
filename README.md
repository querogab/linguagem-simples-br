# linguagem-simples-br

**Linguagem Simples** é uma forma de comunicar que organiza palavras, estrutura e design para ajudar o público a encontrar, entender e usar a informação de que precisa.

Skill para revisar textos em **Linguagem Simples** no português do Brasil.

Ela ajuda a encontrar problemas de estrutura, frases e vocabulário, reescreve o que atrapalha a leitura e inclui uma conferência para evitar a perda de fatos, prazos, condições e referências legais. Foi construída com base na **ABNT NBR ISO 24495-1:2024**, no [Manual de Linguagem Simples da Câmara dos Deputados](https://bd.camara.leg.br/bd/handle/bdcamara/41947) e na [Lei 15.263/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm).

> **Beta pública (`v0.6.0-beta.3`).** A instalação e a integridade do pacote foram verificadas de forma reproduzível no OpenCode `1.18.33`. A skill também foi instalada e usada com sucesso no Claude Code e no Codex. O teste com leitores do público-alvo continua pendente. Veja o [CHANGELOG](CHANGELOG.md).

## Veja um exemplo

**Antes**

> O parâmetro para que uma aplicação financeira possa ser enquadrada como CEC é que: possua a finalidade de atender a compromissos de caixa de curto prazo e não investimento ou outros fins, seja prontamente conversível em quantia conhecida de caixa, no curto prazo e esteja sujeita a risco insignificante de mudança de valor.

**Depois**

> Para que uma aplicação financeira seja classificada como equivalente de caixa (CEC), ela precisa:
>
> - ter a finalidade de atender a compromissos de caixa de curto prazo (e não investimento ou outros fins)
> - ser prontamente conversível em uma quantia conhecida de caixa, no curto prazo
> - estar sujeita a risco insignificante de mudança de valor

A sigla foi expandida e os três critérios ficaram separados. Nenhuma condição foi retirada. Este par veio de uma saída da v0.5.1 e foi conferido contra o [Manual de Contabilidade Aplicada ao Setor Público](.agents/skills/linguagem-simples-br/exemplos/02-mcasp-aplicacoes.md). Ele mostra uma transformação pontual e não dispensa validação técnica do conteúdo contábil.

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

### Interfaces web

Para gerar todos os ZIPs a partir da mesma fonte canônica, sem manter outra cópia editável da skill:

```bash
python scripts/gerar-pacotes-web.py
```

#### Claude web e Cowork

O upload do Claude usa `skill.md` em minúsculas e limita a descrição a 200 caracteres.

Depois, em **Customize > Skills**, escolha **Upload a skill** e envie `dist/linguagem-simples-br-claude-web-cowork-0.6.0-beta.3.zip`. A [Anthropic documenta](https://support.claude.com/en/articles/12512180-use-skills-in-claude) o recurso nos planos Free, Pro, Max, Team e Enterprise e o uso da mesma skill no chat e no Cowork. A execução de código precisa estar habilitada; organizações podem restringir uploads.

#### Gemini web

Em uma conta pessoal com Skills liberadas, abra **Skills**, envie `dist/linguagem-simples-br-gemini-web-0.6.0-beta.3.zip` e habilite a skill. O pacote conserva o `SKILL.md` e os recursos na raiz, como pede a [documentação do Gemini Apps](https://support.google.com/gemini/answer/17094296). O recurso está em implantação gradual e pode ainda não aparecer em todas as contas.

#### ChatGPT web

[Contas elegíveis](https://help.openai.com/articles/20001066) do ChatGPT Business, Enterprise, Healthcare e Edu podem abrir **Plugins > Skills > Create > Upload from your computer** e enviar `dist/linguagem-simples-br-chatgpt-skill-0.6.0-beta.3.zip`.

O gerador também cria `dist/linguagem-simples-br-chatgpt-plugin-0.6.0-beta.3.zip`, um plugin mínimo para distribuição da skill no ChatGPT web. Publicar o plugin no diretório da OpenAI exige o [processo próprio de submissão e revisão](https://developers.openai.com/plugins/deploy/submission).

Os quatro ZIPs passam por conferência de estrutura, integridade, versão e caminhos antes de serem gravados. O upload e o comportamento no Claude web, no Cowork, no Gemini web e no ChatGPT web ainda não foram testados nesta beta.

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

## O que os testes mostraram

Os testes fizeram perguntas diferentes. A primeira foi: **qual instrução produz menos frases longas?** A segunda: **qual delas preserva todos os itens de um texto legal?** Separar as duas evita tratar frase curta como sinônimo de texto fiel ou fácil de entender.

Na v0.5.1, cinco gêneros de texto público foram revisados de três formas:

1. só o modelo, sem instrução adicional;
2. o modelo com um prompt de oito linhas;
3. o modelo com a skill.

Cada forma rodou uma vez por texto, no mesmo modelo e em uma janela separada.

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

As contraprovas da beta verificaram problemas específicos encontrados no uso. Nelas, a skill:

- manteve uma citação literal;
- preservou numeração, modalidade e prazo;
- marcou um referente ausente em vez de inventar a informação.

Em outro teste de escopo, a skill recusou apresentar um rascunho como Leitura Fácil pronta e explicou a validação necessária. O modelo sem a skill falhou nesse ponto nos dois modelos testados.

### Como interpretar

Se o único objetivo é encurtar frases, o prompt de oito linhas foi suficiente e teve o melhor resultado. A skill acrescenta um fluxo de diagnóstico, conferência e tratamento de casos como Leitura Fácil, modalidade e contexto legal brasileiro. Os testes ainda não permitem afirmar que ela melhora a compreensão do público.

Os números vêm da v0.5.1 e não são atribuídos automaticamente à beta atual. Como cada condição rodou uma vez, também não há uma taxa geral de acerto nem uma estimativa de variação entre rodadas.

O [plano de testes](testes/plano-de-testes.md), o [critério de cobertura](testes/gabarito-cobertura.md), o [`medir.py`](testes/medir.py) e os [resultados](testes/resultados/) estão publicados. As conclusões acima usam apenas testes com condições isoladas e materiais que podiam ser publicados. Resultados contaminados por contato prévio com a skill ou baseados em textos sem permissão clara de redistribuição foram excluídos.

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

## Referências

A fundamentação da skill e os links para as obras consultadas estão na seção [Referências do `SKILL.md`](.agents/skills/linguagem-simples-br/SKILL.md#referências). A presença nessa lista indica fonte de consulta, não participação das autoras ou instituições no desenvolvimento deste projeto.
