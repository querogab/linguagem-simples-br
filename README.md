# linguagem-simples-br

Skill para revisar textos em **Linguagem Simples (LS)** no português do Brasil.

Segue o [Manual de Linguagem Simples da Câmara dos Deputados](https://bd.camara.leg.br/bd/handle/bdcamara/41947) (Patricia Roedel, 2024), a norma **ABNT NBR ISO 24495-1:2024** e a [Lei 15.263/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm), que instituiu a Política Nacional de Linguagem Simples.

> **Última versão publicada: v0.6.0-beta.2.** Esta árvore contém correções de auditoria ainda não publicadas. O pacote corrigido precisa de nova instalação reproduzida antes da próxima versão. O teste com leitores continua pendente. Os números desta página vêm da v0.5.1 e não são atribuídos automaticamente à beta. Ver [CHANGELOG](CHANGELOG.md).

Outros contextos também usam os termos **linguagem cidadã** e **linguagem clara**. Aqui vale "linguagem simples", o termo da norma ABNT e da lei brasileira.

## Para que serve

Revisa textos para que o público consiga **encontrar, entender e usar** a informação sem reler nem pedir ajuda a especialista.

Funciona bem em comunicação institucional (site, e-mail, comunicado, FAQ, edital), material educativo e texto jurídico, técnico ou administrativo dirigido a leigo.

Não serve para:

- Texto final de marca pessoal sem uma segunda revisão de voz. A LS pode melhorar a clareza, mas não substitui o estilo da marca.
- **Leitura Fácil** para pessoas com deficiência intelectual. Outro público, outras diretrizes.
- Linguagem neutra de gênero, que é outro tema e está vedada em órgão público pela própria Lei 15.263/2025.
- Texto literário.

## Como instalar

A skill está na pasta [`.agents/skills/linguagem-simples-br/`](.agents/skills/linguagem-simples-br/). O pacote usa o formato Agent Skills. A beta.2 publicada foi instalada e testada no OpenCode 1.18.33; o pacote corrigido desta árvore ainda precisa repetir essa verificação. Compatibilidade com outras ferramentas permanece esperada pelo formato, não garantida.

**Se você usa terminal:**

```bash
npx skills add querogab/linguagem-simples-br
```

**Se você não usa terminal** (e não precisa usar):

1. Baixe a pasta completa `.agents/skills/linguagem-simples-br/`, incluindo `LICENSE`, `THIRD_PARTY_NOTICES.md`, `references/` e `exemplos/`.
2. No OpenCode, copie a pasta para `.opencode/skills/` no projeto. No Claude Code, use `.claude/skills/` no projeto ou `~/.claude/skills/` para uma instalação global.
3. Feche e abra a ferramenta depois da cópia. Arquivos de configuração não são recarregados na sessão em andamento.

**Em uma ferramenta que não carrega Agent Skills:** cole o conteúdo do `SKILL.md`, sem o cabeçalho entre `---`, no campo de instruções. Esse caminho manual funciona, mas ainda não foi testado como instalação desta beta.

Depois de instalada, ela funciona de dois jeitos: **sozinha**, quando você pede para revisar ou simplificar um texto, ou **chamada pelo nome**, com um pedido como `Use a skill linguagem-simples-br`.

## Como usar

```
Use a skill linguagem-simples-br para revisar este texto:
[cole o texto]
```

O que ela faz, na ordem:

1. Descobre pelo contexto do projeto se o texto é de órgão público, onde a Lei 15.263/2025 obriga LS, ou privado, onde é boa prática.
2. Pergunta público, suporte e objetivo do leitor. Só o que ainda não deu para inferir.
3. Diagnostica em quatro frentes: burocratês, arquitetura, frases, palavras.
4. Reescreve, decidindo primeiro o que **não** mudar.
5. Entrega a versão final e os avisos necessários. A tabela antes/depois, a avaliação pelos 4 princípios da ISO 24495-1 e a recomendação de teste ficam sob demanda, salvo em modo didático ou texto de órgão público.

Para aprender enquanto revisa, peça `me ensina os 3 principais`, `me ensina tudo` ou `me ensina sobre [diretriz]`.

Para texto de órgão público, o apêndice [`references/lei-15263-tecnicas.md`](.agents/skills/linguagem-simples-br/references/lei-15263-tecnicas.md) mapeia as 18 técnicas do art. 5º da PNLS com checklist. A lista do artigo é exemplificativa ("tais como"), não taxativa.

Cinco pares curtos e conferidos estão em [`exemplos/`](.agents/skills/linguagem-simples-br/exemplos/README.md). São resultados históricos da v0.5.1, identificados como tal, não saídas reexecutadas na beta.

## O que ela não promete

Prometer o que a medição nega é o defeito que esta lista existe para evitar. O que ficou de fora:

**Não promete frases mais curtas que um prompt de 8 linhas.** Perde, e perde nas cinco. O confronto está nas duas tabelas abaixo: o prompt curto zera a cauda e chega a uma mediana de 11,8 palavras contra 14,6 da skill. Em tamanho de frase, ela é overhead.

**Não promete cobrir mais fatos que o prompt curto.** Isso foi testado em dois artigos de lei com listas fechadas, o art. 5º da Lei 15.263 (18 incisos) e o art. 46 da Lei 9.610 (11 itens, quatro deles alíneas aninhadas). **As três condições cobriram tudo: 18 de 18 e 11 de 11.** Nenhuma perdeu as condições que fazem a exceção legal valer, como *sem intuito de lucro* e *um só exemplar*.

A única diferença apareceu nas **remissões**: a skill citou as 8 do texto, o prompt curto 7 e a revisão comum 6. O item que separa a skill do prompt curto é o **art. 7º, que foi vetado**, e artigo vetado não tem conteúdo: omiti-lo numa reescrita para o cidadão é escolha editorial defensável. **Tirado ele, os dois empatam em 7 de 7**, e a revisão comum fica em 6. **O critério de contagem está publicado** em [`testes/gabarito-cobertura.md`](testes/gabarito-cobertura.md), escrito antes da rodada e afrouxado depois dela, quando 5 marcas rígidas demais produziram falso negativo.

O mesmo critério foi passado nas rodadas antigas, em dois modelos e na versão v0.3 da skill: **18 de 18 em todas.** Uma versão anterior deste README dizia que a skill cobria 16 de 18 e ficava atrás. **Era erro de contagem, e está corrigido.**

**Não encurta o texto.** O volume entregue fica praticamente igual ao de uma revisão comum. O que muda é a distribuição do tamanho das frases, não o total.

**Não deixa as frases mais curtas em média.** A mediana quase não se move, e isso é de propósito. O freio manda não mexer em frase que já está clara, e a frase mediana geralmente está. A skill troca "encurta tudo um pouco" por "não estraga o que estava bom".

**Não resolve tudo.** Numa passagem do texto da BNCC sobre tecnologias digitais, nenhuma condição conseguiu quebrar a frase, em rodada nenhuma. O contraexemplo está guardado em [`testes/`](testes/plano-de-testes.md).

## O que ela entrega, medido

Cinco gêneros de texto público, cada um revisado em três condições, no mesmo modelo e em janelas separadas. A terceira condição é um **prompt curto de 8 linhas** que pede frases de até 20 palavras, voz ativa e nenhum fato perdido. Ele está aqui porque é o concorrente honesto de qualquer skill de simplificação.

### 1. Ela mata a cauda de frases longas, e o prompt de 8 linhas mata mais

Contagem e distribuição do tamanho das frases são **proxies de legibilidade**, não medida direta de compreensão. Só teste com leitores mostra se o público encontra, entende e usa a informação.

| Frases acima de 30 palavras | original | modelo sozinho | prompt de 8 linhas | com a skill |
|---|---|---|---|---|
| Material educativo (BNCC) | 77,8% | 26,7% | **0,0%** | 11,8% |
| Manual técnico (MCASP) | 38,5% | 4,8% | **0,0%** | 4,8% |
| Edital (UECE) | 21,4% | 6,7% | **0,0%** | **0,0%** |
| FAQ de pregão (MDH) | 46,7% | 7,7% | **0,0%** | **0,0%** |
| Ofício-circular (CVM) | 35,7% | 13,3% | **0,0%** | **0,0%** |
| **média** | **44,0%** | **11,8%** | **0,0%** | **3,3%** |

A skill derruba a cauda em relação a uma revisão comum, e a frase mais longa encolheu em 4 dos 5 textos. O prompt de 8 linhas faz melhor: zera os cinco. A média das frases máximas por texto foi 21,4 palavras no prompt curto e 29,4 na skill; as maiores frases individuais tiveram 25 e 41 palavras, respectivamente.

**Qual é a régua.** Frase aqui é o que fica entre ponto, ponto-e-vírgula, dois-pontos, exclamação ou interrogação. Essa definição está implementada no [`medir.py`](testes/medir.py); mudar a segmentação também muda os números.

**O 3,3% é um ponto, não uma faixa.** Cada célula é uma execução. Uma linha só, a do material educativo, responde por 71% da média. Versões diferentes da skill mediram 2,5%, 5,9% e 3,3%; isso mostra que as mudanças de regra movem o resultado, mas não estima a variação da v0.5.1. Uma faixa de repetição pediria várias execuções da mesma versão por célula, e elas não foram feitas.

Está escrito assim de propósito. Se tudo o que você quer é frase curta, **oito linhas resolvem, e você não precisa desta skill**. O que ela tem de diferente vem agora.

### 2. Ela foi desenhada para evitar mudanças sem ganho de clareza

Pedir revisão de um texto que já está bom é o caso em que uma ferramenta de reescrita tem mais a perder. Por isso, a skill manda identificar primeiro o que deve permanecer intacto. Esse comportamento ainda precisa de uma nova avaliação pública com material cuja redistribuição seja inequívoca; não há taxa de acerto publicada para ele.

## O que diferencia esta skill

Legenda honesta: ✅ testado, e o modelo sem skill falhou · 🟡 não testado, é conteúdo que o modelo não teria como saber · ❌ testado, e o modelo sem skill também passa.

- ✅ **Marca a fronteira com Leitura Fácil e diz a regra que decide.** Pedida uma adaptação para LF, a skill recusa, explica a diferença e nomeia o que nenhuma outra condição nomeou: material de Leitura Fácil só é Leitura Fácil depois de validado por um grupo de pessoas com deficiência intelectual. Ela entrega rascunho para validação, nunca produto pronto. Nos cenários de escopo, foi o único item em que o modelo sem skill falhou, e falhou nos dois modelos testados. *(Este resultado sai da rodada por subagentes, a mesma em que se achou vazamento de contexto num outro cenário. O vazamento empurraria a linha de base a recusar, como a skill faz; ela não recusou. O defeito trabalha contra este resultado, e por isso ele fica.)*
- ✅ **Não atribui a ninguém um exemplo que a pessoa não escreveu.** Citação de obra só com o texto em mãos, transcrita e com fonte. Três citações do Manual da Câmara foram conferidas página a página.
- 🟡 **Foi desenhada para não mexer no que já está claro.** O mecanismo existe, mas ainda precisa de uma avaliação pública com material redistribuível que reúna frases curtas e longas.
- 🟡 **Derruba a cauda de frase longa** em relação a uma revisão comum (11,8% para 3,3%). Marcado em amarelo de propósito: o prompt de 8 linhas faz isso melhor, então é ganho sobre o pedido comum, não diferencial da skill.
- 🟡 **Camada legal brasileira.** As 18 técnicas do art. 5º da Lei 15.263/2025 com o caput tratado como exemplificativo, a fronteira do art. 6º, o art. 7º vetado e a regulamentação por ente do art. 8º.
- 🟡 **Ancorada em norma, não em opinião.** ABNT NBR ISO 24495-1:2024 e o Manual da Câmara. A adaptação ABNT da ISO existe, o que as referências internacionais não têm.
- 🟡 **Trata teste com leitor real como etapa**, com 4 métodos e a regra de que colega de time não serve de leitor.
- 🟡 **Diagnóstico antes da reescrita e aviso quando o problema não é de linguagem.** O cenário que descartava esses itens como diferencial foi reaberto porque as condições de controle herdaram o formato da skill. Eles continuam como recursos, sem alegação de superioridade.
**Sobre as partes setoriais da ISO 24495.** Esta skill foi construída e validada somente contra a parte 1. As partes setoriais para comunicação jurídica e científica estão fora do escopo atual.

### Comparada à outra skill brasileira de simplificação

A [`humanizar`](https://github.com/fabricioctelles/skills) (Apache-2.0, ativa) é uma skill anti-*AI slop* que tem "Português Simplificado" como um dos perfis de voz, fundada no PorSimples e no NILC-Metrix. Quem procurar simplificação em português vai achar as duas.

A diferença: lá a LS é um perfil dentro de uma ferramenta de humanização; aqui ela é o objeto inteiro, com norma ISO, diagnóstico separado da reescrita, distinção entre texto público e privado, modo didático e teste com leitor. Este repositório não redistribui o corpus citado pela outra skill.

## Como isto foi medido

Todo número ainda publicado acima vem dos arquivos preservados em [`testes/`](testes/plano-de-testes.md). Resultados baseados em material que não pode ser redistribuído com segurança foram retirados do pacote público e das alegações desta página.

**Desenho.** Cada texto rodou em três condições, no mesmo modelo e em janelas separadas: sem a skill, com a skill, e com o prompt de 8 linhas. O modelo é o sujeito do teste e nunca avalia o próprio resultado.

🔴 **Uma das rodadas teve vazamento de contexto, e está escrito aqui porque foi medido.** As tabelas acima vêm das rodadas feitas à mão, uma janela por condição. Houve outra rodada, em outro modelo, despachada por subagentes a partir de uma sessão que já tinha lido a skill. Num dos cinco cenários dela, **as duas condições de controle entregaram o formato de saída da skill**, com a seção de avaliação pela ISO incluída, coisa que o prompt de 8 linhas não pede em nenhuma das suas oito linhas. O plano de teste tinha previsto esse risco por escrito e o desenho não o impediu. Nenhum número desta página sai daquele cenário.

**Textos.** São 8 entradas de documentos públicos brasileiros e um cenário autoral sintético. A origem de cada uma está registrada no plano de testes. Nenhum texto pessoal nem material de cliente foi incluído. O controle do medidor usa um trecho de notícia da Agência Senado, reproduzido sem alteração e nunca reescrito, com origem e autorização em [`testes/controle/README.md`](testes/controle/README.md). Veja também os [`avisos sobre material de terceiros`](THIRD_PARTY_NOTICES.md).

**Instrumento.** O [`medir.py`](testes/medir.py) é descritivo, não é nota de qualidade e não deve virar alvo de otimização. Já levou nove correções: a primeira medição lia tabela como uma frase de 212 palavras e premiava quem entregava prosa em vez de estrutura.

Ele leva um controle positivo a cada mudança. Em 06/09/26 ganhou um **segundo controle**, com tabela, título, lista e regra horizontal, porque o positivo é prosa pura e por isso não tocava o trecho de código que mais mudou: cinco dos nove defeitos moravam lá e nenhum foi pego por regressão. O controle novo achou um defeito **na primeira execução**, e o defeito tinha direção: a regra horizontal `---` nunca era descartada e colava na frase seguinte, e só a condição com skill entrega `---`. Consertado e recalculado, **nenhum número desta página mudou**.

**A tabela antes/depois reprovou na auditoria histórica e passou no candidato.** As saídas da v0.5.1 traziam contagens não verificadas e, no FAQ, respostas inferidas sem apoio no original. Na `v0.6.0-beta.1`, uma nova execução teve 8 de 8 originais literais e 8 de 8 revisões presentes na versão final, sem contagem inventada nem resposta categórica criada. É um caso em um modelo, não uma taxa. Ver as [`NOTAS.md`](testes/resultados/2026-09-28__beta-comportamental/NOTAS.md).

**O que os números não separam.** Cada condição rodou uma vez. Entre duas rodadas em que a skill mudou em 3 linhas, o volume de texto de processo dobrou, o que dá a medida do ruído entre execuções. Diferença de décimo não se lê. O que sustenta as conclusões é a direção repetida em vários textos e a coincidência com o modo de falha previsto antes de rodar.

## Roadmap

- ✅ v0.2: ajustes pós-autoteste (9 atritos)
- ✅ v0.3: pesquisa expandida sobre LS no Brasil, 1 correção factual e o apêndice da Lei 15.263
- ✅ v0.4 *(05/09/26)*: três consertos de defeito medido, entre eles a validação obrigatória da Leitura Fácil e a trava de fidelidade
- ✅ v0.5 / v0.5.1 *(05–06/09/26)*: trava de modalidade e freio de sobre-edição, este subordinado à régua objetiva de tamanho de frase
- ✅ **v0.6.0-beta.1:** pacote com referência legal e cinco exemplos conferidos; quatro casos comportamentais aprovados; descoberta automática e instalação pública reproduzidas no OpenCode
- **v0.6.0-beta.2:** quatro ajustes derivados de uso real em edital, com contraprovas para estrutura e fidelidade; teste com leitores pendente
- v1.0: comportamento da beta validado com uso externo e leitor do público-alvo; documentação fechada
- v1.1: README bilíngue, templates por gênero, modo "revisar resposta de IA", evals

Os números de versão mudaram de significado em 05/09/26. O roteiro antigo prometia "v0.4 = feedback de uso real" e "v0.5 = exemplos antes/depois"; o que saiu foram consertos de defeito medido. Está corrigido aqui para o que aconteceu.

## Licença

O código, a skill e a documentação autoral estão sob **MIT**. Trechos de documentos-fonte e o controle da Agência Senado não são relicenciados pela MIT. As origens, os limites e as autorizações aplicáveis estão em [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Contribuições

Abra uma issue com caso de uso, problema encontrado ou sugestão. Texto que deu errado na revisão é o tipo de contribuição mais útil.

## Créditos

- **Patricia Roedel**, Manual de Linguagem Simples da Câmara dos Deputados
- **Heloísa Fischer**, pioneira de Linguagem Simples no Brasil, [Comunica Simples](https://comunicasimples.com.br)
- **ICICT/Fiocruz**, Guia de Linguagem e Design Simples
- **International Plain Language Federation**, definição internacional de Plain Language
