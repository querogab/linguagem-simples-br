# Gabarito de cobertura de fato

> 🔴 **Escrito em 06/09/26, às 10h, ANTES de qualquer saída da rodada existir.** É a condição que faz o teste valer: gabarito montado depois de ver o resultado é critério desenhado para o resultado que apareceu.
>
> **O que ele mede:** de quantos itens enumerados do texto original a revisão ainda dá conta. Não mede se ficou bonito, nem se ficou curto. **Só se o fato sobreviveu.**

## Por que a unidade é "item enumerado"

"Fato" é palavra elástica e vira julgamento meu. **Item enumerado não é.** Os dois textos deste teste trazem listas fechadas na origem — 18 incisos num, 11 itens no outro — e cada item carrega um conteúdo distinto. Contar quantos sobreviveram é verificável por outra pessoa, que é o teste de um instrumento.

⚠️ **Cobertura não é o mesmo que fidelidade.** Um texto pode citar todos os 18 incisos e ainda assim dizer algo errado sobre um deles. Este gabarito pega **omissão**, não **distorção**. A distorção continua sendo achada por leitura, e isso está dito de propósito.

## O isolamento, e como saber se ele furou

A rodada acontece numa **sala limpa** fora desta árvore, pasta que contém só os 2 textos e uma cópia da skill. **Este arquivo não está lá.** A garantia deixa de ser *"não leia"* e passa a ser *"não alcança"*: quem segura é a fronteira de diretório da ferramenta, não a obediência do modelo.

📌 **E os prompts da rodada não citam este arquivo nem por nome.** Dizer *"não leia o gabarito"* é anunciar que existe um gabarito — a proibição é que planta a ideia.

⚠️ **Se mesmo assim furar, fica rastro.** Modelo que viu a lista de checagem tende a usar as marcas aceitas **na forma literal**, em vez de parafrasear. **Antes de aceitar qualquer número, conferir a taxa de literalidade:** saída que bate 18 de 18 usando exatamente as minhas palavras é **suspeita, não sucesso**.

## 🐛 Defeito do instrumento, achado em 06/09/26 às 10h40 — e o que ele prova

Na primeira contagem, o script acusou **7 candidatos a omissão**. **Cinco eram falsos negativos meus**, todos da mesma família: a marca estava numa forma e o texto usou outra.

| item | minha marca | o que o texto escreveu |
|---|---|---|
| T1 III | *uma ideia por parágrafo* | *"cada parágrafo deve ter uma ideia só"* |
| T1 X | *mais importante primeiro* (singular) | *"as informações mais importantes primeiro"* |
| T1 XIV | *substantivo no lugar de verbo* (singular) | *"substantivos no lugar de verbos"* |
| T2 VII | *prova judiciária* (a palavra da lei) | *"prova judicial"*, *"provas judiciais"* |
| T2 condição | *sem intuito de lucro* | *"sem intenção de lucro"* |

⭐ **A regra 3 se pagou na primeira uso.** *"Todo candidato é lido antes de virar número"* — sem ela, eu teria publicado **base 15/18** quando a base cobre **18/18**, e a conclusão do teste sairia invertida.

📌 **O sinal que denunciou:** os itens X e XIV apareceram como omitidos **nas três condições ao mesmo tempo**. Item que "some" em todo mundo quase nunca sumiu — **é a régua que não alcança**. Vale como heurística geral: *falha unânime acusa o instrumento, não o objeto.*

✅ **Consertado:** as marcas viraram expressão regular tolerante a plural e a variante (`substantivos? no lugar (de|do)s? verbos?`), e a tabela abaixo já está na forma corrigida.

## Como pontuar

1. O script procura, para cada item, **qualquer uma** das marcas aceitas.
2. Item sem nenhuma marca vira **candidato a omissão**, nunca omissão confirmada — paráfrase legítima não tem por que usar minhas palavras.
3. **Todo candidato é lido antes de virar número.** O número final é o da leitura, não o do script.
4. **Cobertura parcial conta como coberta** se o núcleo do item aparece. Exemplo: o inciso XI tem o Volp, o Acordo Ortográfico e o Decreto 6.583; se a revisão disser "não invente flexão de gênero fora das regras da língua", o item está coberto. **Perder a remissão ao decreto é outro defeito, contado à parte.**

---

## T1 — Lei 15.263/2025, art. 5º · 18 incisos

| # | núcleo do inciso | marcas aceitas (qualquer uma) |
|---|---|---|
| I | frase em ordem direta | ordem direta · sujeito antes · começar pelo sujeito |
| II | frases curtas | `frases? (mais )?curtas?` · `encurtar frases?` |
| III | uma ideia por parágrafo | `uma ideia (por\|em cada) parágrafo` · uma ideia só · uma única ideia |
| IV | palavras comuns | palavra comum · palavra do dia a dia · fácil compreensão · palavra simples |
| V | sinônimo ou explicação de termo técnico | sinônimo · jargão · termo técnico · explicar no texto |
| VI | evitar estrangeirismo | estrangeir · palavra de outra língua · palavra em inglês |
| VII | não usar termo pejorativo | pejorativ · termo ofensivo · palavra que ofende |
| VIII | nome completo antes da sigla | sigla · nome completo antes |
| IX | listas, tabelas, recursos gráficos | lista · tabela · recurso gráfico · esquemátic |
| X | informação importante primeiro | `mais importantes? primeiro` · `importantes? (no\|em) começo` · informação principal |
| XI | não criar flexão de gênero e número | flexão · gênero · Volp · Acordo Ortográfico · 6.583 · linguagem neutra |
| XII | voz ativa | voz ativa · quem faz a ação |
| XIII | evitar frase intercalada | intercalad · frase no meio · aposto longo |
| XIV | não usar substantivo no lugar de verbo | `substantivos? no lugar (de\|do)s? verbos?` · nominaliza · `substantivos? abstratos?` |
| XV | evitar redundância | redundân · palavra desnecessária · repetição inútil |
| XVI | evitar palavra imprecisa | impreci · palavra vaga · termo genérico |
| XVII | acessibilidade para pessoa com deficiência | deficiência · acessív · acessibilidade · 13.146 · Estatuto |
| XVIII | testar com o público-alvo | testar com · público-alvo · validar com leitor |

**Remissões legais deste texto, contadas à parte:** Decreto 6.583/2008 · Volp · Acordo Ortográfico · Lei 13.146/2015 · Estatuto da Pessoa com Deficiência · art. 6º (comunidades indígenas) · art. 7º vetado · art. 8º (cada ente federativo).

⚠️ **O inciso XI é o mais fácil de perder por conveniência**, porque trata de linguagem neutra e o assunto é politicamente carregado. **Perder XI é omissão como qualquer outra**, e vale a pena olhar se alguma condição o perde mais que as outras.

---

## T2 — Lei 9.610/1998, art. 46 · 11 itens

Estrutura diferente de propósito: o inciso I tem quatro alíneas, então o teste também pega **aninhamento perdido**, que é o modo de falha típico de quem "organiza" uma lista.

| # | núcleo | marcas aceitas |
|---|---|---|
| I-a | notícia ou artigo na imprensa, com menção ao autor e à publicação | imprensa · notícia · artigo informativo · nome do autor |
| I-b | discurso em reunião pública | discurso · reunião pública |
| I-c | retrato feito sob encomenda, pelo dono do objeto | retrato · encomenda · imagem |
| I-d | obra para uso de pessoa com deficiência visual, em Braille | Braille · deficiente visual · deficiência visual |
| II | cópia de pequeno trecho, um exemplar, uso privado, sem lucro | um exemplar · uso privado · copista · sem lucro |
| III | citação para estudo, crítica ou polêmica, indicando autor e fonte | citação · estudo · crítica · polêmica |
| IV | apanhado de lições por quem assiste à aula | apanhado · lição · aula · anotação |
| V | uso em estabelecimento comercial, só para demonstrar à clientela | estabelecimento comercial · demonstração · clientela |
| VI | teatro e música em casa ou em escola, sem lucro | teatral · musical · recesso familiar · didátic |
| VII | uso para produzir prova judiciária ou administrativa | `provas? judicia(l\|is\|ria\|rias)` · prova administrativa · processo judicial |
| VIII | pequeno trecho em obra nova, quando não é o objetivo principal | pequeno trecho · obra preexistente · artes plásticas |

**As condições que acompanham cada item e são fáceis de sumir:** *sem intuito de lucro* / *sem intenção de lucro* / *sem lucro* (II, V, VI) · *menção ao nome do autor* (I-a, III) · *um só exemplar* (II) · *vedada a publicação sem autorização* (IV) · *sem fins comerciais* (I-d).

📌 **Estas condições são o teste de verdade do T2.** Quem "simplifica" lista de exceção legal tende a entregar a exceção e comer a condição — e uma exceção sem a condição **inverte a regra**.
