# Cobertura de fato — re-teste (06/09/26)

**6 execuções**, 2 textos × 3 condições, rodadas em sala limpa fora do projeto. O gabarito ([`gabarito-cobertura.md`](../../gabarito-cobertura.md)) foi escrito às 10h, **antes de a rodada existir**.

---

## 🔴 Leia primeiro: o número que este teste veio conferir estava errado

Este teste existia para checar um achado de 04/09: *"a skill escreveu 3× mais e cobriu menos"* — **skill 16/18 · base 17/18 · micro 18/18**.

**Remedi as três rodadas com o mesmo gabarito, e o 16/18 não existe.** Os incisos VII e XV estão na *"3. Versão final limpa"* do `C1__skill.md` do Opus, **linhas 86 e 88, marcados pela própria skill**:

> *"Cortar o que se repete e o que não faz falta. **(XV)**"*
> *"Não usar termos que ofendam ou diminuam alguém. **(VII)**"*

🔴 **Foi erro de contagem na leitura de 04/09**, e ele virou conclusão de destaque — e virou **justificativa da trava de fidelidade da v0.4**. Corrigido em **8 documentos** em 06/09/26.

### O quadro completo, um instrumento só, com leitura em cima

| C1 / T1 — art. 5º, 18 incisos | base | skill | micro |
|---|---|---|---|
| Opus 5, 04/09 (skill v0.3) | 18/18 | **18/18** | 18/18 |
| deepseek, 04/09 (skill v0.3) | 18/18 | **18/18** | — |
| deepseek, 06/09 (skill v0.5.1) | 18/18 | **18/18** | 18/18 |
| T2 — art. 46, 11 itens, 06/09 | 11/11 | **11/11** | 11/11 |

✅ **Empate no teto em tudo:** 2 modelos, 2 versões da skill, 2 textos, 3 condições.

### 📌 E a linha "Modelo:" dos arquivos não vale como registro

Dois arquivos desta rodada declaram **GPT-4o**, mas todas as execuções usaram **deepseek**. ⚠️ **A linha foi escrita pelo modelo, e modelo não sabe qual modelo é** — preencheu o campo com o palpite mais plausível. Outro arquivo do projeto traz `deepseek/depseek-v4-flas`, **com typo**: quem lê um identificador não o digita errado, quem **gera** digita.

✅ **O registro válido é o do cliente usado na execução.** O campo `**Modelo:**` sai dos próximos prompts ou passa a ser preenchido por quem executa o teste.

## O resultado: empate no teto

| | T1 — 18 incisos | T2 — 11 itens | T2 — 5 condições |
|---|---|---|---|
| base | **18/18** | **11/11** | **5/5** |
| micro | **18/18** | **11/11** | **5/5** |
| skill v0.5.1 | **18/18** | **11/11** | **5/5** |

🔑 **As três condições cobriram tudo, nos dois textos** — e o mesmo vale para as rodadas de 04/09 quando remedidas com este gabarito. **Não é caso de "não se reproduziu": o achado antigo era erro de contagem**, como está no topo.

⚠️ **O que segue sendo verdade é o outro lado da linha antiga:** a skill **escreve muito mais texto**. Isso foi medido e nunca desmentido. **Só não vem acompanhado de perda de fato.**

## Onde apareceu diferença: as remissões legais do T1

| remissão | base | micro | skill v0.5.1 |
|---|---|---|---|
| Decreto 6.583/2008 | 🔴 **perdeu** | ✅ | ✅ |
| Volp | ✅ | ✅ | ✅ |
| Acordo Ortográfico | ✅ | ✅ | ✅ |
| Lei 13.146/2015 | ✅ | ✅ | ✅ |
| Estatuto da Pessoa com Deficiência (nome) | trocou por *Lei Brasileira de Inclusão* | só o número | ✅ nome e número |
| art. 6º — comunidades indígenas | ✅ | ✅ | ✅ |
| art. 7º **vetado** | 🔴 **perdeu** | 🔴 **perdeu** | ✅ |
| art. 8º — cada ente federativo | ✅ | ✅ | ✅ |
| **total** | **6/8** | **7/8** | **8/8** |

📌 **A troca de *Estatuto* por *Lei Brasileira de Inclusão* não é perda** — são dois nomes oficiais da mesma lei, e o número foi dado. Contei como coberta.

⚖️ **E o *art. 7º vetado* é discutível.** Um artigo vetado não tem conteúdo; omiti-lo numa reescrita para o cidadão é escolha editorial defensável. **O que ele informa é que a lei tem um buraco ali** — quem lê a versão da base ou do micro não fica sabendo. Vale registrar como diferença, não como erro.

---

## 🔮 A previsão que eu escrevi antes de rodar: 1 certa, 2 erradas

| previsão | resultado |
|---|---|
| T1: a skill empata ou melhora | ✅ **certa** — empatou, 18/18 nas três |
| T2: todas perdem alguma alínea do inciso I | ❌ **errada** — as três cobriram as 4 alíneas |
| Condições (*sem lucro*): o micro perde mais | ❌ **errada, e é a que mais dói** — o micro preservou **as cinco** |
| Remissão legal: todas preservam | 🟡 **quase** — a skill preservou 8/8, o micro 7/8, a base 6/8 |

🔴 **A terceira era a que sustentaria o segundo argumento da skill.** A hipótese era: *"o prompt curto encurta cortando a condição, e a condição decide a quem a regra se aplica"*. **Não aconteceu.** O micro entregou frases de até 20 palavras e mesmo assim manteve *sem intuito de lucro*, *um só exemplar*, *menção ao nome do autor*, *sem fins comerciais* e *vedada a publicação sem autorização*.

⭐ **Então esse argumento não existe, e não entra no README.** A previsão escrita antes é o que permitiu descobrir isso em vez de procurar confirmação depois.

---

## 🐛 O instrumento errou primeiro, e a regra 3 pegou

A primeira contagem acusou **7 candidatos a omissão**. **Cinco eram falsos negativos meus** — marca no singular contra texto no plural, *judiciária* contra *judicial*, *sem intuito de lucro* contra *sem intenção de lucro*.

Sem a regra *"todo candidato é lido antes de virar número"*, eu teria publicado **base 15/18** quando a base cobre **18/18** — e a conclusão sairia invertida.

📌 **O sinal que denunciou:** dois itens apareceram omitidos **nas três condições ao mesmo tempo**. **Falha unânime acusa o instrumento, não o objeto.** Está anotado no gabarito como heurística.

---

## Veredicto

✅ **Em cobertura de fato, as três condições empatam no teto.** A skill não perde fato, e o critério *"não perder nenhum fato"* pode ficar no README — **mas como algo que ela cumpre, não como algo em que ela ganha.**

🔴 **O que o README deixou de dizer:** que o prompt curto cobre mais. **Ele nunca cobriu** — o número que dizia isso era erro de contagem.

✅ **E não fica pendente nada aqui.** A dúvida de modelo se resolveu sozinha: remedi as pastas de 04/09 com o mesmo gabarito, então **existe comparação no mesmo modelo (deepseek 04/09 × deepseek 06/09) e no outro (Opus 5)** — e as três dizem 18/18. **Zero execução nova.**
