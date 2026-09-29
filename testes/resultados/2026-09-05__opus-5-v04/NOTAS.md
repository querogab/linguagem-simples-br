# NOTAS — v0.4, re-teste dos 3 consertos

**Rodada:** 05/09/26, 08h20 · **Modelo:** claude-opus-5 (subagentes, contexto frio)
**Escopo:** só o braço `skill`. **`base` e `micro` NÃO foram refeitos** — os 3 consertos não os afetam, então valem os resultados de [`../2026-09-04__opus-5/`](../2026-09-04__opus-5/) como linha de base. Re-teste custou **5 execuções em vez de 15**.

> 🔑 É o ganho concreto de ter registrado linha de base com data: quando só o tratamento muda, só o tratamento roda de novo.

---

## 📊 A comparação

| Cen. | condição | palavras | média | máx | >30 |
|---|---|---:|---:|---:|---:|
| **C1** | base | 752 | 11,9 | 44 | 3,3% |
| | micro | 521 | 9,6 | 24 | 0,0% |
| | skill **v0.3** | 1.644 | 13,5 | **71** ⚠️ | 6,7% |
| | skill **v0.4** | **1.274** | **11,5** | **41** | **1,8%** |
| **C2** | base | 1.134 | 11,6 | 54 | 5,2% |
| | micro | 416 | 9,2 | 19 | 0,0% |
| | skill **v0.3** | 707 | 14,1 | 48 | 4,0% |
| | skill **v0.4** | **659** | **12,6** | **30** | **0,0%** |
| **C3** | base | 598 | 12,5 | 37 | 2,1% |
| | micro | 453 | 8,2 | 17 | 0,0% |
| | skill **v0.3** | 1.497 | 13,2 | 38 | 3,5% |
| | skill **v0.4** | **1.229** | **11,7** | 45 | **1,0%** |
| **C4** | base | 345 | 7,1 | 14 | 0,0% |
| | micro | 210 | 7,7 | 12 | 0,0% |
| | skill **v0.3** | 900 | 11,0 | 36 | 1,2% |
| | skill **v0.4** | **767** | **9,9** | 56 ⚠️ | 2,6% |
| **C5** | base | 1.030 | 11,9 | 34 | 2,3% |
| | micro | 936 | 10,1 | 28 | 0,0% |
| | skill **v0.3** | 1.273 | 12,2 | 42 | 3,8% |
| | skill **v0.4** | 1.366 | **12,0** | 41 | **0,9%** |

---

## ✅ Conserto 2 (trava de fidelidade) — o resultado da rodada

**C1, cobertura dos 18 incisos do art. 5º:**

| | cobertura | palavras |
|---|---|---:|
| base | 17/18 (faltou XV) | 778 |
| micro | **18/18** | 575 |
| skill **v0.3** | **16/18** (faltaram VII e XV) | 2.413 |
| skill **v0.4** | ✅ **18/18** | **2.048** |

🔴 **CORRIGIDO EM 06/09/26: a skill nunca saiu de 16/18 — ela já estava em 18/18.** 🔴 **ERRO DE CONTAGEM, corrigido em 06/09/26 às 11h.** Os incisos **VII e XV não foram perdidos**: estão na *"3. Versão final limpa"* do `C1__skill.md`, linhas 86 e 88, **marcados pela própria skill com *(VII)* e *(XV)***. *"Cortar o que se repete e o que não faz falta. (XV)"* · *"Não usar termos que ofendam ou diminuam alguém. (VII)"*. **Remedido com o mesmo gabarito nas três rodadas: cobertura é 18/18 em todas as condições, nos dois modelos, nas duas versões da skill.** ▸ [`gabarito-cobertura.md`](../../../testes/gabarito-cobertura.md) ✅ **O que continua de pé nesta linha é o encolhimento de 15%**, esse sim medido. *(Texto original abaixo.)*

🎯 **A skill saiu de 16/18 para 18/18 e ainda encolheu 15%.** Empatou com o micro-prompt no critério em que estava perdendo — e era o defeito mais grave que a medição de 05/09 achou, porque *"não perder nenhum fato"* é critério da própria skill.

A trava operável ("18 incisos entram, 18 saem — **contar, não estimar**") resolveu o que a formulação vaga anterior ("não cortar nuance") não pegava.

## ✅ Conserto 3 (saída enxuta) — funcionou, com uma exceção

| | v0.3 → v0.4 | micro |
|---|---|---:|
| C1 | 1.644 → **1.274** (**−23%**) | 521 |
| C2 | 707 → **659** (−7%) | 416 |
| C3 | 1.497 → **1.229** (**−18%**) | 453 |
| C4 | 900 → **767** (−15%) | 210 |
| C5 | 1.273 → **1.366** (**+7%**) | 936 |

⚠️ **O C5 cresceu**, contra a direção pretendida. Motivo aparente na leitura: a v0.4 achou **mais problema de jornada** que a v0.3 — inclusive um que a versão anterior não tinha visto (*"são duas idas presenciais, em janelas de 3h e 2h"*). O aviso de processo é bloco de **avisos**, que o modo enxuto mantém de propósito. **Crescer porque encontrou mais é diferente de crescer por enfeite** — mas o número sozinho não distingue os dois casos, e por isso está anotado aqui em vez de comemorado.

📌 **A skill continua 2–3× mais longa que o micro-prompt.** O conserto reduziu a distância, não a eliminou.

## ✅ Conserto 1 (validação da Leitura Fácil) — saiu do acaso

Na v0.3 o modelo **inventou sozinho** o argumento da validação; não estava no arquivo, então não havia garantia de reaparecer. Agora está escrito, e apareceu — com um ganho que não estava previsto: o modelo intitulou o bloco **"Rascunho para validação (ainda não é Leitura Fácil)"**, o que faz a ressalva sobreviver se alguém copiar só aquele trecho.

## ✅ Sem regressão na trava de citação (C2)

A recusa ficou **mais** explícita, já no título da seção: *"Exemplo do Manual da Câmara para cada uma — isso eu não vou entregar"*, seguido de *"não estou com o Manual da Patricia Roedel aberto nesta sessão"*. O modo enxuto não afrouxou a trava.

---

## Onde a skill continua atrás

🔴 **O micro-prompt segue ganhando em tamanho de frase e em volume nos cenários medidos.** Os consertos fecharam a lacuna de **fidelidade** (18/18 × 18/18) e reduziram a de volume, mas não invertem o quadro de 05/09. **A §7.1 do plano continua valendo: o README não pode prometer clareza nem frase curta.**

⚠️ **Um dado piorou:** o `C4__skill` tem máx 56 contra 36 na v0.3, e 2,6% acima de 30 contra 1,2%. Uma execução por célula não distingue isso de variação da amostra — **anotado, não interpretado.**

## Conclusão

**Os 3 consertos entregaram o que prometiam, e cada um mirava defeito medido — nenhum foi regra acrescentada por suposição.** O método se sustentou: medir, consertar só o que a medição apontou, re-medir contra a mesma linha de base.

✅ **5/5 executados.** 📉 **Volume caiu em 4 dos 5 cenários** (−23%, −18%, −15%, −7%), e o único que subiu (C5, +7%) subiu porque **achou mais problema de jornada**, não por enfeite.

⏳ **Falta:** uma rodada com **3 execuções por célula** para separar sinal de ruído — trabalho de v1.1. Até lá, **só a direção vale**, e ela é consistente: 4 de 5 cenários encolheram e a fidelidade fechou em 18/18.
