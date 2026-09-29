# NOTAS — rodada Opus 5

**Rodada:** iniciada 04/09/26 21h04, completada 05/09/26 08h05
**Modelo:** claude-opus-5 (subagentes, contexto frio)
**Condições:** C1–C5 × base / skill / micro = 15 execuções

> 🔑 Esta rodada existe porque a de 04/09 (DeepSeek) saiu com **texto corrompido** e com **acesso desigual a fontes** entre as condições. Ver [`../2026-09-04__deepseek-v4-flash/AUDITORIA.md`](../2026-09-04__deepseek-v4-flash/AUDITORIA.md).

## Como esta rodada corrigiu o desenho

1. **Mesmo acesso a fontes nas três condições** — nenhuma consulta material externo nem busca na internet. Na rodada anterior, `skill` tinha acesso à lei e ao manual e `base` não, o que transformou o C2 numa comparação *com fonte × sem fonte*.
2. **Resposta limpa** — pedi saída sem cabeçalho de metadado e sem autocomentário. Na rodada anterior esses blocos entravam na medição e o próprio comentário virava "achado".
3. **Medição só da resposta**, com markdown descartado e sinalizador `>60 palavras`.
4. **Sem corrupção de texto.** Confere-se por leitura: os arquivos estão em português íntegro.

⚠️ **O que continua fora:** cada condição rodou **uma vez**. Sem repetição, diferença pequena entre condições não é distinguível de variação da amostra. Trate ordens de grandeza, não decimais.

---

## 📊 Medição

| Cenário | base | skill | micro |
|---|---|---|---|
| | média / máx / >30 | média / máx / >30 | média / máx / >30 |
| C1 | 11,9 / 44 / 3,3% | 13,5 / **71** ⚠️ / 6,7% | **9,6 / 24 / 0,0%** |
| C2 | 11,6 / 54 / 5,2% | 14,1 / 48 / 4,0% | **9,2 / 19 / 0,0%** |
| C3 | 12,5 / 37 / 2,1% | 13,2 / 38 / 3,5% | **8,2 / 17 / 0,0%** |
| C4 | 7,1 / 14 / 0,0% | 11,0 / 36 / 1,2% | 7,7 / 12 / 0,0% |
| C5 | 11,9 / 34 / 2,3% | 12,2 / 42 / 3,8% | **10,1 / 28 / 0,0%** |

🔴 **O micro-prompt vence nos 5 cenários, e com 0% acima de 30 palavras em todos.** A skill fica **atrás da própria linha de base** em 5 de 5. Isso replica o resultado do C6 da rodada DeepSeek, agora sem corrupção, sem contaminação de markdown e em modelo diferente. **É o achado mais sólido das duas rodadas.**

⚠️ O `C1__skill` tem uma unidade de 71 palavras que o sinalizador marcou — conferir antes de citar esse número isolado.

**Volume:** a skill produz 2 a 4× mais texto (C4: 900 palavras contra 345 da base e 210 do micro). Custo real de leitura, não só de token.

---

## 🔴 Os dois diferenciais de ontem NÃO se reproduziram

Esta é a parte que muda o plano. Na rodada DeepSeek, C4 e C5 foram registrados como "diferença absoluta" a favor da skill. **Em Opus, as três condições se comportam igual.**

### C4 — fronteira de escopo: a base já sabe

- **base:** produziu Leitura Fácil direto, sem avisar que é outro escopo.
- **micro:** idem — e ainda **definiu "cidadão", "parágrafo" e "jargão"** dentro do texto, que é técnica de LF.
- **skill:** ✅ recusou como fronteira, explicou a diferença em tabela **e acrescentou o argumento mais forte dos três**: *"material de Leitura Fácil só é Leitura Fácil depois de validado por um grupo de pessoas com deficiência intelectual"* — e entregou como rascunho para validação, não como produto pronto.

📌 **A skill ainda ganha aqui, mas por um motivo diferente do que estava escrito.** O diferencial não é *recusar* — é **nomear a validação obrigatória**. Nenhuma das outras duas mencionou. É um ponto de conteúdo, não de postura.

### C5 — problema de processo: as três avisaram

**As três condições identificaram o laço e recomendaram escalar**, incluindo a `base` sem instrução nenhuma:

> **base:** *"Reescrever este texto vai deixá-lo mais claro, mas não vai resolver o principal. O processo descrito tem três travas..."*
> **micro:** *"O texto está confuso em parte porque o processo é apertado. Três pontos que a reescrita não resolve..."*

🔴 **Pela regra do `SimpleEnglish` — "critério que a linha de base já passa não prova nada" — o C5 tem que ser DESCARTADO como diferencial.** Ele não distingue nada em Opus. Manter como critério de qualidade da skill seria comemorar o que o modelo já faz sozinho.

⚠️ **Ressalva honesta:** o C5 *distinguiu* em DeepSeek. Então o resultado correto é **"depende do modelo"** — o Passo 2 da skill segura o comportamento em modelo mais fraco e é redundante em modelo forte. Isso é diferente de "inútil", e é exatamente o que o [relatório de auditoria do SimpleEnglish](https://github.com/AminBlg/SimpleEnglish/blob/main/evals/results/WHY-USELESS-2026-09-02.md) descreve: a linha de base subiu por baixo da skill.

---

## Fidelidade (C1) — o que a rodada anterior não conseguiu medir

Todas as remissões legais sobreviveram nas três condições: Decreto 6.583/2008, Lei 13.146/2015, o art. 7º vetado e o art. 6º das línguas indígenas. **Nenhuma perda de remissão** — a alegação do `NOTAS` de ontem sobre isso não se reproduz.

Cobertura dos 18 incisos do art. 5º:

| Condição | incisos cobertos | ausentes |
|---|---|---|
| base | 17/18 | XV (redundâncias) |
| **skill** | ~~**16/18**~~ → **18/18** 🔴 | ~~VII · XV~~ **erro de contagem, corrigido em 06/09/26 — os dois estão na "3. Versão final limpa", linhas 86 e 88, marcados *(VII)* e *(XV)* pela própria skill** |
| **micro** | **18/18** | — |

🔴 **A skill perdeu mais conteúdo que as outras duas, apesar de escrever 3× mais.** Conferido por leitura, não só por busca. Isso é grave: o critério "não perder nenhum fato" é da própria skill, e a condição `micro` — que traz esse critério em **uma linha** — foi a única a cumprir 18/18.

---

## Conclusão

1. 🔴 **O micro-prompt ganha em tamanho de frase nos 5 cenários e em fidelidade no C1.** Replicado em dois modelos. Não é ruído.
2. 🔴 **C5 sai da lista de diferenciais** — a base já passa.
3. ✅ **C4 continua diferencial, mas reformulado:** o que só a skill entrega é a **validação obrigatória por pessoas com deficiência intelectual**, não a recusa em si.
4. ✅ **A trava contra citação forjada segue valendo** (verificada na rodada DeepSeek, página a página).
5. ⚠️ **A skill escreve 2–4× mais e cobre menos** do art. 5º. Volume não é entrega.

**O que isso pede do plano:** a §7 (critérios de sucesso) e a seção "em que difere" do README não podem se apoiar em C5 nem em "textos mais claros". Sobram como diferenciais reais: a **camada legal brasileira**, a **fronteira LS ≠ Leitura Fácil com a regra de validação**, a **trava de citação** e o **encaminhamento**. É uma lista mais curta e mais honesta do que a de ontem.
