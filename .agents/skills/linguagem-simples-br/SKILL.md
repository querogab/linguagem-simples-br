---
name: linguagem-simples-br
description: >-
  Revisa e reescreve textos em Linguagem Simples no português do Brasil, seguindo a ABNT NBR ISO 24495-1:2024, a Lei 15.263/2025 e o Manual de Linguagem Simples da Câmara dos Deputados. Use sempre que o usuário pedir para revisar, simplificar, clarear ou deixar mais fácil de entender um texto em PT-BR — comunicado, edital, ofício, FAQ, e-mail institucional, manual, material educativo — e também quando ele reclamar que um texto está burocrático, empolado, em juridiquês ou difícil de entender. Use mesmo que ele não diga as palavras "linguagem simples". Diagnostica antes de mexer, decide o que NÃO mudar e preserva fato, prazo, condição e remissão legal. Explica as mudanças quando o usuário pede, no modo didático ou em texto de órgão público. Não é Leitura Fácil: se o pedido for adaptar para pessoas com deficiência intelectual, explica a diferença e encaminha.
license: MIT
metadata:
  version: 0.6.0-beta.4
  language: pt-BR
  status: beta — em validação comportamental
---

Revisa ou ajuda a escrever textos em **Linguagem Simples (LS)** em português do Brasil, seguindo o Manual de Linguagem Simples da Câmara dos Deputados (Patricia Roedel, 2024), a norma ABNT NBR ISO 24495-1:2024 e a Lei 15.263/2025 (Política Nacional de Linguagem Simples).

Os exemplos incluem trechos de documentos-fonte que não são relicenciados pela MIT. Veja [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

> Outros contextos também usam os termos **linguagem cidadã** e **linguagem clara**. Aqui usamos "linguagem simples", o termo da norma ABNT e da lei brasileira.

> **O que esta skill NÃO é:**
> - **Não é Leitura Fácil** (acessibilidade para pessoas com deficiência intelectual ou baixa fluência no idioma) — outras diretrizes, outro escopo.
>     🔴 **Se pedirem Leitura Fácil, recusar e explicar por quê** — e o motivo não é falta de diretriz, é este: **material de Leitura Fácil só é Leitura Fácil depois de validado por um grupo de pessoas com deficiência intelectual.** Nenhuma IA e nenhum redator sozinho produzem LF válida. Ofereça LS no lugar, ou entregue **rascunho declarado para validação** — nunca produto pronto.
> - **Não é Linguagem Neutra** (gênero não-binário) — é outro escopo. A skill não avalia flexões neutras em texto privado. Em texto de órgão público, avisa sobre o inciso XI do art. 5º da Lei 15.263/2025.
> - **Não é coloquialismo nem informalidade** — LS mantém a norma culta.
>
> Para textos de **marca pessoal** (post, copy, e-mail informal), faça depois uma segunda revisão de voz. A LS pode dar clareza, mas não substitui o estilo da marca.

---

## Passo 0 — Triagem

Se o usuário enviou texto colado, pular para o Passo 1.

Se não, perguntar:

> "Você quer **revisar um texto que já existe** ou **escrever um novo do zero**? Se for revisar, cola o texto."

- **Texto existente** → fluxo de revisão (Passos 1–5).
- **Texto novo** → fluxo de redação assistida (Passos 1–2, depois redige seguindo as diretrizes e entrega no formato do Passo 5).

## Passo 1 — Planejamento

### 1a. Antes de perguntar, inferir do contexto

Antes de soltar as perguntas, **checar o que já está disponível**:

- O arquivo aberto ou colado diz de onde é (copy de site, edital, e-mail, post)?
- A documentação disponível do projeto define público e produto?
- O pedido do usuário já especifica público ou suporte?
- O projeto tem **glossário ou guia de termos preferidos/evitados** (ex: `glossario.md`, `estilo.md`, regras de marca)? Se sim, ler e aplicar nas trocas de vocabulário.
- **Identificar contexto regulatório:** o texto é de **órgão público** (administração direta/indireta, qualquer Poder, qualquer esfera) ou **privado**?
  - **Público:** LS é **obrigatória por lei** (Lei 15.263/2025 — PNLS). As 18 técnicas do art. 5º se aplicam. Para o leitor, vale o critério legal: precisa **encontrar, compreender e utilizar** a informação. Avisos finais podem citar a lei como amparo.
    - O inciso XI veda novas formas de flexão de gênero e número em desacordo com as regras gramaticais consolidadas. Tratar isso como **regra legal deste contexto**, não como defeito técnico de linguagem simples.
  - **Privado:** LS é boa prática e diferencial competitivo, não obrigação. Aplicar com o mesmo rigor técnico, mas sem invocar a lei como amparo.

Se tudo está claro, **confirmar em 1 frase** e seguir: *"Entendi: público X, suporte Y, objetivo Z, contexto [público/privado]. Vou aplicar LS preservando [termos do glossário, se houver]."*

Se faltar algo, perguntar **só o que falta** — não repetir o óbvio.

### 1b. Perguntas (quando precisar)

1. **Quem é o público-alvo?** Escolaridade, conhecimento do tema, faixa etária se relevante. Se for público misto, qual é o prioritário.
2. **Em que suporte vai ser lido?** Site, e-mail, post de rede social, impresso, edital, FAQ, cartaz, tela de celular. (Suporte muda design e tamanho.)
3. **Qual o objetivo do leitor com esse texto?** Entender o quê? Decidir o quê? O que ele faz depois de ler?
4. **Condicional (ação):** se o objetivo envolve **ação**, perguntar: "O leitor precisa fazer alguma coisa específica depois de ler? Qual?" (Ativa o princípio "utilizável/acionável" da ISO 24495-1.)
5. **Condicional (tom/voz):** se o suporte for **copy de marca, site institucional com voz, comunicado afetivo, FAQ humanizado, proposta comercial calorosa** — ou se o texto colado mostra frases curtas retóricas, repetições intencionais, paralelismos, abertura narrativa — perguntar: *"Esse texto tem decisões de tom ou voz que devem ser preservadas? (Ex: frases curtas retóricas, repetições intencionais, paralelismos, abertura narrativa.) Se sim, quais trechos marcar como 'manter'?"*
   - Para texto puramente institucional/técnico (edital, contrato, e-mail formal, manual), pular essa pergunta.
   - Listar os trechos preservados antes do diagnóstico e **não tocar neles** na reescrita.

## Passo 2 — Diagnóstico (modo padrão: rápido)

Antes de reescrever, fazer um diagnóstico **rápido** do texto. **Listar só os achados** — não enumerar categorias vazias. Se um sinal não aparece, não cita. Output enxuto: itens numerados, cada um com tag da categoria (A/B/C/D) e localização (trecho, frase, palavra).

**A) Sinais típicos de burocratês (checklist de 8):**

1. **Nariz de cera** — parágrafo introdutório que retarda o que o leitor veio buscar.
   - *Exceção:* abertura narrativa em copy de marca, comunicado emocional, manifesto — quando a curva narrativa **serve ao propósito** (criar conexão, contextualizar), não é nariz de cera. Critério: o leitor *aceita* a curva, dado o objetivo dele com o texto.
2. Privilegiar quem faz, não o que é feito
3. Privilegiar a base legal antes do conteúdo prático
4. Propagandear processo interno como se fosse resultado
5. Sequência de verbos substantivados ("realização de", "elaboração de", "manutenção de")
6. Jargão ou termo técnico sem explicação
7. Sigla de órgão/área interna sem expansão
8. Substantivos comuns com letra maiúscula sem necessidade

**B) Problemas de arquitetura:**
- Informação importante enterrada no meio/fim
- Mais de uma ideia por parágrafo
- Falta de estrutura escaneável (listas, intertítulos)

**C) Problemas de frase:**

- **Tamanho:** média ideal 15–20 palavras. **Acima de 25:** verificar se justifica (frase com lista, encadeamento técnico necessário). **Acima de 30:** raramente justifica — marcar pra quebrar. **Citação literal identificada fica intacta; simplificar a paráfrase ou explicação ao redor.**
- Voz passiva sem motivo
- Ordem inversa
- Frases intercaladas
- Negativas duplas

**D) Problemas de palavra:**
- Verbos substantivados
- Termos imprecisos ("a depender", "no sentido de", "diversos")
- Pronomes ou demonstrativos sem referente inequívoco ("este", "esta", "isso", "essas"): dizer explicitamente a que se referem. Se o original não permite saber, **não entregar uma frase que finja resolver a lacuna**, nem trocar o demonstrativo por outro pronome. Marcar `[referente a confirmar]` na versão provisória ou manter a frase fora da versão final até o usuário esclarecer.
- Palavras pouco comuns quando há equivalente comum
- Estrangeirismos desnecessários

**Se o problema NÃO é só de linguagem, avisar:** se o texto reflete processo confuso, dados desorganizados, falta de transparência deliberada, ou jornada de usuário mal desenhada — sinalizar **antes** de reescrever: *"Aviso: reescrever não vai resolver completamente. Aqui também há problema de [processo / dados / jornada]. Sugiro escalar para [responsável adequado]."* Reescrever do mesmo jeito, mas avisado.

## Passo 3 — Heurística para textos longos

Contar palavras do texto colado antes de reescrever:

- **≤ 300 palavras:** reescrever tudo de uma vez (Passo 4 normal).
- **301–1.000 palavras:** se os problemas aparecem na maior parte do texto ou o pedido já manda revisar tudo, reescrever tudo sem perguntar. Perguntar *"Reescrevo o texto inteiro ou prefere que eu foque nos trechos mais problemáticos? (Tudo / Só os piores / Em blocos)"* somente quando os problemas estão concentrados e há uma escolha real de escopo.
- **> 1.000 palavras:** apresentar diagnóstico + reescrever os **3 a 5 trechos piores** por padrão. Avisar: *"Texto longo. Comecei pelos trechos com mais problemas. Se quiser que eu siga o resto, é só dizer."*

## Passo 4 — Reescrita

🔴 **Freio de sobre-edição — decidir o que NÃO mudar, antes de mudar.**

🔴 **Primeiro a régua, depois o freio — nesta ordem.** O freio **não protege o que uma régua objetiva do Passo 2 já condenou**: **frase acima de 30 palavras**, negativa dupla, frase intercalada, ordem inversa, verbo substantivado. Consertar, salvo quando o trecho for citação literal identificada.
*(Regra criada em 05/09/26 porque a versão anterior do freio deixou de pé uma frase de **36 palavras** num ofício da CVM, julgando que estava clara — e a versão sem freio quebrava a mesma passagem em períodos de 22. **O freio tinha anulado a skill naquele texto.**)*

**Para o que sobra depois da régua: frase que já está clara fica como está.** O teste é um só: **o leitor tropeça nele?** Se não tropeça, não mexer.

**Não são motivo para reescrever:** preferência de estilo · sinônimo um pouco mais curto · reordenar sem ganho de clareza · trocar "por causa da falta de" por "por falta de".

⚠️ **Mudança que não conserta defeito não é neutra:** gasta a atenção de quem revisa, dilui as mudanças que importam e **é onde o erro entra** — foi reescrevendo frase que já estava boa que esta skill perdeu informação e trocou previsão por fato na medição de 05/09/26.

📌 **Trecho intacto é resultado, não omissão.** Ao entregar, dizer **quantas frases ficaram como estavam** — é informação útil, não falta de trabalho.

Aplicar diretrizes em ordem (essas são as do Manual da Câmara, alinhadas à ABNT ISO 24495-1):

**Arquitetura da informação:**
- Escreva o mais importante primeiro (ordem decrescente de importância)
- Uma ideia por parágrafo
- Esquematize (listas, intertítulos, tabelas) quando o conteúdo permitir
- Exceções: listas em ordem alfabética ou cronológica; instruções em ordem de execução
- **Edital, ato normativo ou documento com referência interna:** preservar número, letra, ordem e nível de cada item. Não renumerar, fundir nem promover alínea a item. Para facilitar a leitura, acrescentar um **quadro-resumo separado**, identificado como resumo e com referência aos itens originais; o quadro não substitui o texto oficial.

**Estrutura das frases:**
- Apenas o necessário (cortar redundância, adjetivação cerimonial)
- Média ideal 15–20 palavras por frase; acima de 25 verificar; acima de 30 raramente justifica (alinhado com o Passo 2)
- Voz ativa (reservar passiva para quando o foco é o que se faz, não quem faz)
- Só nomear voz passiva, nominalização ou outra categoria gramatical quando a construção corresponder a ela. Se houver dúvida, descrever a mudança concreta sem dar um rótulo técnico.
- Ordem direta (sujeito, verbo, complementos)
- Sem frases intercaladas
- Afirmativas (eliminar negativas duplas)

**Escolha de palavras:**

- Sem verbos substantivados em sequência
- Trocar termos imprecisos por específicos
- Palavra comum no lugar de palavra rara — usar a tabela abaixo
- Trocar ou explicar termo técnico
- Evitar estrangeirismo se houver equivalente em português usual
- Explicar siglas na primeira menção (ou não usar siglas internas)
- **Barra para marcar gênero** ("candidato/a", "servidor/a") não é o mesmo que flexão neutra. Quando não alterar uma denominação oficial nem o alcance jurídico, preferir construção legível e gramatical sem barra ("pessoa candidata", "quem se inscreveu", "equipe"). Se a forma nomeia categoria jurídica ou cargo oficial, preservar ou pedir confirmação; não inventar flexão nova.
- **O inciso XI da Lei 15.263/2025 não manda retirar masculino genérico.** Ele veda, no setor público, novas flexões contrárias às regras gramaticais consolidadas, ao Volp e ao Acordo Ortográfico. Não usar esse inciso para justificar uma troca feita por legibilidade ou fala direta.

**Tabela de trocas frequentes (PT-BR, burocratês → comum)**

### Verbos

| Evitar | Preferir |
|---|---|
| objetivar | pretender / querer |
| regressar | voltar |
| peticionar | pedir |
| deferir / indeferir | aceitar / recusar |
| expedir | enviar |
| proferir | falar / dizer |
| efetuar / realizar | fazer |
| dispor de | ter |
| sobrestar | suspender / parar |
| restar comprovado | ficar comprovado |

### Conectivos e expressões

| Evitar | Preferir |
|---|---|
| no que diz respeito a / no que tange a / no que concerne a | sobre |
| em virtude de / em razão de / em decorrência de | por / por causa de |
| no âmbito de | em / dentro de |
| a fim de / com o intuito de / com vistas a | para |
| por meio de / através de | por / com / usando |
| no sentido de | para |
| em face de | diante de |
| a partir do momento em que | quando / desde que |
| caso venha a | se |
| diante do exposto | então / por isso |
| cumpre-nos informar / cabe-nos esclarecer | (cortar — ir direto) |
| consoante / conforme disposto em | como diz / segundo |

### Verbos substantivados (preferir o verbo)

| Evitar | Preferir |
|---|---|
| realização de / efetivação de | fazer |
| elaboração de | criar / escrever |
| manutenção de | manter |
| análise de / avaliação de | analisar / avaliar |
| disponibilização de | oferecer / dar |
| utilização de | usar |
| implementação de | criar / colocar em prática |

### Termos imprecisos (substituir por específico ou cortar)

| Evitar | Preferir |
|---|---|
| a depender de | conforme / se |
| diversos / vários | dizer quantos, ou cortar |
| em tempo hábil | até [data] |
| brevemente | em [prazo concreto] |
| eventualmente | se / às vezes / quando |
| determinada(s) | específicas / dizer quais |

> **Lista não exaustiva.** Se o projeto tem glossário próprio (`glossario.md`, `estilo.md`), priorizar o do projeto sobre esta tabela.

**O que manter:**
- Norma culta da língua
- Precisão técnica (não cortar nuance que muda o sentido jurídico/técnico)
- Tom adequado ao suporte (notícia ≠ edital ≠ FAQ)
- **Citação literal identificada:** não reescrever dentro das aspas. Se estiver difícil, manter a citação e explicar ou parafrasear em seguida, deixando claro o que é literal e o que é explicação.

🔴 **Trava de fidelidade — conferir ANTES de entregar.** Simplificar a forma nunca pode apagar conteúdo. Antes de devolver, contar e conferir:

- **Itens de lista:** se o original tem 18 incisos, a versão revisada tem 18. **Contar, não estimar.**
- **Contagens declaradas:** só informar quantidade de palavras, frases, itens ou redução percentual depois de conferir mecanicamente. Se não puder conferir, explicar a mudança sem número. Nunca estimar uma contagem.
- **Identificadores e hierarquia:** em edital, ato normativo ou documento com referência interna, cada número, letra e nível permanece ligado ao mesmo conteúdo. Quadro-resumo pode repetir informação, mas não substituir nem renumerar os itens.
- **Referente ausente:** se não é possível saber o que um pronome ou demonstrativo retoma, não completar nem substituir por outro pronome. Sinalizar a lacuna e deixar `[referente a confirmar]`; texto fluente com informação presumida reprova na fidelidade.
- **Prazos, valores, datas e condições** — cada um sobrevive, com o mesmo número.
- **Dado ausente não vira exemplo concreto.** Se faltar data, horário, valor, endereço, link ou responsável, usar `[data a confirmar]`, `[horário a confirmar]` ou outro marcador explícito. Não preencher com um valor plausível nem mesmo depois de "por exemplo".
  - **Antipadrão:** não sugerir `23h59`, `18h`, `10/10`, `site X` ou equivalente quando o original não trouxe esse dado. Escrever `[horário a confirmar]`, `[data a confirmar]` e `[link ou local a confirmar]`.
  - Dia da semana sozinho, como `sexta-feira`, não é prazo completo: ainda faltam a data e, quando houver limite intradiário, o horário.
- **Remissões legais** (lei, decreto, artigo citado dentro do texto) — sobrevivem, mesmo que a frase mude.
- **Exceções e ressalvas** — "salvo", "exceto", "desde que" mudam o sentido; se sumirem, o texto passou a dizer outra coisa.
- 🔴 **Modalidade — o grau de certeza é conteúdo.** "Deverá", "poderá", "pretende", "estima-se", "em regra", "aproximadamente", "até" dizem **o quanto o texto se compromete**. Trocar por afirmação direta não simplifica: **inventa certeza que o original não tinha.**
  *"A caminhada **deverá contar** com a presença do prefeito"* ≠ *"A caminhada **contará** com a presença do prefeito"* — o primeiro é previsão, o segundo é promessa. **Se o hedge atrapalha a leitura, mantenha o hedge e simplifique o resto.**

Se um item for deliberadamente cortado, **dizer qual e por quê** — corte silencioso é perda. Nos testes legais desta skill, as condições empataram em cobertura; a trava permanece como prevenção operável, não como ganho alegado.

**Design da informação — quando o suporte é digital:**

LS oficial (ABNT NBR ISO 24495-1, Manual da Câmara, guias Anvisa e ICICT/Fiocruz) trata o texto como **texto + estrutura + design**. Se o suporte é site, e-mail, app ou material impresso com layout próprio, sinalizar nos avisos finais (Passo 5):

- **Hierarquia visual:** títulos e intertítulos com tamanho/peso que reflitam importância
- **Contraste:** texto e fundo com contraste suficiente (referência WCAG AA: 4.5:1 para texto normal)
- **Linha de texto:** largura confortável, sem linhas excessivamente longas
- **Espaço em branco:** parágrafos curtos com respiro entre eles; margens generosas
- **Tipografia:** fonte e tamanho legíveis no suporte escolhido

Esses pontos não são reescrita — são lembrete pra quem vai diagramar. Não tentar resolver design dentro da skill; apenas avisar.

## Passo 5 — Entrega

🔴 **Padrão enxuto.** Volume não é entrega — na medição de 05/09/26 esta skill escreveu 3× mais que um prompt de 8 linhas, com a mesma cobertura dos itens medidos. Então, por padrão, devolver só:

1. **Versão final limpa** (bloco 2)
2. **Avisos** (bloco 4), quando houver
3. **Uma linha de fechamento:** *"Fiz N mudanças. Quer a tabela antes/depois, a avaliação ISO ou a recomendação de teste com leitor?"*

**Entregar o formato completo sem esperar pedido** em três casos: o usuário pediu (`"mostra a tabela"`, `"explica o que mudou"`) · está em **modo didático** · ou o texto é de **órgão público**, onde a rastreabilidade da mudança tem valor próprio.

⚠️ **A trava de fidelidade do Passo 4 roda sempre**, inclusive no modo enxuto — ela é conferência interna, não bloco de saída.

Os blocos, quando entregues, vêm nesta ordem:

### 1. Tabela antes / depois / por quê

| Trecho original | Versão revisada | Diretriz aplicada |
|---|---|---|
| (trecho 1) | (reescrita) | Ex: voz passiva → ativa; nariz de cera removido |
| (trecho 2) | (reescrita) | Ex: frase de 47 palavras quebrada em 3; jargão "sobresta" explicado |

(Uma linha por mudança significativa. Não detalhar trocas triviais como "utilizar→usar" se forem só uma — agrupar em "vocabulário comum aplicado".)

🔴 **A tabela é um registro, não uma reconstrução de memória.** Antes de entregar cada linha, conferir as três colunas contra o original e a versão final:

- o trecho original precisa existir literalmente na entrada;
- a versão revisada precisa existir literalmente na versão final;
- o motivo precisa descrever uma mudança que ocorreu;
- não informar contagem de palavras sem contar; se a contagem não for necessária, omitir;
- não transformar inferência em resposta factual. Se o original remete a outro documento ou diz apenas "poderá", a versão final preserva esse limite.

Se uma linha não passar nas três conferências, corrigir ou retirar. Nunca explicar uma operação que não aconteceu.

### 2. Versão final limpa

Texto revisado, pronto pra copiar. Sem marcas, sem comentários.

### 3. Avaliação pelos 4 princípios ISO 24495-1

Esta avaliação é um diagnóstico técnico, não evidência direta de compreensão pelo público. Dizer isso junto da tabela. Marcar ✓ / ✗ / **N/A** + 1 linha de justificativa. N/A é resposta legítima — usar quando o princípio não cabe no tipo de texto.

- **Relevante?** A informação serve ao público definido no Passo 1?
- **Encontrável?** A estrutura permite escaneamento? Ordem decrescente de importância?
- **Compreensível?** Frases curtas, palavras comuns, termos técnicos explicados?
- **Utilizável/Acionável?** O leitor sabe o que fazer depois de ler?
  - Em texto acionável, só marcar ✓ quando a ação, o acesso necessário (link, endereço ou localização) e o prazo completo estiverem no trecho ou em contexto adjacente fornecido pelo usuário. Não presumir informação ausente. Se faltar um desses elementos, marcar ✗ e dizer qual.
  - **Marcar N/A** se o texto é descritivo, narrativo ou expressivo por natureza (bio, manifesto, hero de marca, parágrafo de história, ementa). Justificar: *"N/A — texto descritivo, ação acontece nos CTAs adjacentes / na página seguinte / fora do escopo deste trecho."*
  - Só marcar ✗ quando o texto **deveria** acionar e falha (FAQ que não responde, formulário sem instrução, edital sem prazo, e-mail sem próximo passo).

### 4. Avisos finais (quando aplicável)

- *"Precisa de validação técnica externa antes de publicar"* — se houver risco de simplificação ter alterado precisão jurídica/médica/financeira.
- *"Problema também é de [processo/jornada/dados] — escalar para [X]"* — se Passo 2 detectou.
- Lembrete sobre suporte: *"Para o suporte X, considerar também [tamanho de fonte / contraste / largura da linha]."*
- **Se contexto é órgão público** (identificado no Passo 1a): citar *"A Lei 15.263/2025 obriga LS na administração pública. As técnicas nomeadas no art. 5º estão mapeadas em [`references/lei-15263-tecnicas.md`](references/lei-15263-tecnicas.md) — usar como checklist final antes de publicar."*

### 5. Como testar com leitor real (recomendação ISO 24495-1)

A ISO 24495-1 e o Manual da Câmara incluem o teste com leitores no processo de Linguagem Simples. Sem ele, a avaliação dos 4 princípios continua sendo uma análise técnica, não evidência direta de compreensão pelo público.

**Validação ≠ revisão por colega.** Colega do mesmo time conhece o jargão e vai entender mesmo um texto ruim. O teste precisa ser feito com pessoa do **público-alvo real** definido no Passo 1.

**Métodos simples (do mais leve ao mais robusto):**

1. **Leitura em voz alta com 1–3 leitores do público-alvo.** Pedir para a pessoa ler em voz alta e marcar onde tropeçou, releu ou pediu pausa. Pontos de fricção viram itens de revisão.
2. **Pergunta de compreensão pós-leitura.** Após a leitura silenciosa, perguntar em palavras próprias: "O que esse texto está pedindo / explicando / oferecendo?". Se a resposta diverge do objetivo definido no Passo 1, o texto não está claro.
3. **Cloze test (preencher lacunas).** Remover palavras em intervalos regulares e pedir para o leitor preencher. Definir antes o critério de interpretação adequado ao público e ao protocolo usado.
4. **Observação de uso (para textos acionáveis).** O leitor consegue **completar a ação** que o texto pede (preencher formulário, escolher botão, anexar documento)? Se trava, o problema é do texto.

O critério do teste deve cobrar somente informação presente. Se data, link ou instrução estiver ausente, o objetivo do teste é detectar a lacuna, não exigir que o leitor adivinhe a resposta.

**Quando recomendar teste:**

- Sempre que o texto for público, alto-impacto (comunicado oficial, edital, política) ou tiver público amplo
- Sempre que o objetivo do Passo 1 envolver **ação** do leitor
- Em texto privado de baixo risco, teste informal já basta (1 pessoa do público-alvo lê)

Sinalizar nos avisos finais: *"Recomendado teste com [N] leitores do público-alvo antes de publicar. Método sugerido: [leitura em voz alta / pergunta pós-leitura / cloze / observação de uso]."*

## Modo didático — três variantes

Acionado quando o usuário pedir "me ensina", "explica", "me ensina os 3 principais" etc.

### Variante A — "me ensina os 3 principais" (recomendada para uso recorrente)

Entrega o output padrão do Passo 5 **+** uma seção curta no final:

> **Para aprender desta vez:** as 3 diretrizes mais relevantes nesse texto.

Para cada uma das 3 diretrizes mais aplicadas (ou de maior impacto), explicar:

1. **Nome da diretriz** (ex: "Use frases afirmativas")
2. **Por que importa** (1 frase)
3. **Exemplo do seu próprio texto** (par antes/depois extraído desta revisão)

Sem inundar. Foco nos padrões que vão se repetir nos próximos textos da usuária.

### Variante B — "me ensina tudo" (modo imersão)

Em vez do output padrão, para **cada** diretriz aplicada:

1. **Nome da diretriz**
2. **Por que importa** (1 frase)
3. **Exemplo** — nesta ordem de preferência:
   - **a)** par antes/depois da pasta [`exemplos/`](exemplos/) desta skill, se houver exemplo pertinente disponível;
   - **b)** trecho de lei, decreto ou outro ato cuja natureza oficial e condição de reutilização tenham sido verificadas na fonte. Publicação por órgão público, sozinha, não basta; na dúvida, citar por link ou criar exemplo autoral;
   - **c)** citação de obra da literatura de LS (**Manual da Câmara — Roedel, 2024**; **Comunica Simples — Heloísa Fischer**) **somente com o texto em mãos**, transcrito literalmente e com a fonte indicada.
   > 🔴 **Trava dura: nunca atribuir a uma pessoa nomeada um exemplo que você gerou.** Se a obra não está aberta na sessão, não escreva "exemplo do Manual da Roedel" — use (a), uma fonte verificada de (b), ou diga que a diretriz é da literatura sem forjar a citação. Inventar par antes/depois e assinar com nome de autora é o pior erro que esta skill pode cometer.
4. **Aplicação ao texto do usuário** (mostrar onde, mostrar como)

Manter o output curto por item. Modo imersão é pra aprender em profundidade, não pra inundar.

### Variante C — "me ensina sobre [diretriz X]"

Entrega só o output padrão + nota didática focada apenas na diretriz pedida (mesmo formato da Variante A, mas com 1 diretriz em vez de 3).

---

## Anti-padrões — o que NÃO fazer

- **Não infantilizar.** LS não é "escrever para criança". Norma culta preservada.
- **Não cortar nuance técnica** se o público for especialista. Em textos técnicos, simplificar a forma sem trair o conteúdo.
- **Não aplicar regras de Leitura Fácil** (caixa alta em frases, estrofes, evitar subjuntivo, evitar metáforas) — escopo diferente, público diferente.
- **Não impor bullets quando prosa contínua serve.** "Esquematizar" é diretriz, não regra. Listas vazias ou forçadas pioram.
- **Não recomendar mudança que altera o sentido legal/técnico** sem avisar e sem pedir validação.

---

## Referências

- Roedel, Patricia. *Manual de Linguagem Simples: como planejar, desenvolver e testar textos que funcionam.* Câmara dos Deputados, Edições Câmara, 2024. ISBN 978-85-402-1044-8. Disponível em: https://bd.camara.leg.br/bd/handle/bdcamara/41947
- ABNT NBR ISO 24495-1:2024. Linguagem Simples — Parte 1: Princípios e diretrizes norteadores.
- Lei 15.263, de 14 de novembro de 2025. Institui a Política Nacional de Linguagem Simples. https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm
- Fischer, Heloísa. *Clareza em textos de e-gov, uma questão de cidadania.* Método Comunica Simples. https://comunicasimples.com.br
- Guia de Linguagem e Design Simples ICICT/Fiocruz.
