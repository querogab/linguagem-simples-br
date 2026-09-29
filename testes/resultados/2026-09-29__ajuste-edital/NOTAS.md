# Ajuste pós-uso em edital

**Data:** 29/09/26  
**Ferramenta:** OpenCode `1.18.33`  
**Modelo:** `openai/gpt-5.6-sol`  
**Execuções:** três; T7 uma vez e eval 11 antes e depois da correção

## Origem

Um uso real da beta em edital revelou quatro lacunas: pergunta de escopo sem escolha útil, risco de alterar numeração, ausência de regra para barra de gênero e demonstrativo ambíguo não diagnosticado. O edital real e sua saída não entram neste repositório. As contraprovas usam o T7 público e um trecho sintético.

## Resultado

- **T7:** passou em escopo, numeração, ordem e hierarquia. O quadro-resumo não foi acionado.
- **Eval 11, primeira execução:** passou em numeração, modalidade, prazo e barra de gênero; reprovou em fidelidade porque reconheceu o referente ausente e inventou `entregá-las`.
- **Eval 11, depois da correção:** passou nos quatro critérios. Usou `[referente a confirmar]` e não inventou o objeto.

## Consequência

A trava de referente ausente foi endurecida depois da reprovação e a reexecução passou. Foram três execuções de modelo: duas na rodada inicial e uma contraprova adicional depois da falha. Uma chamada anterior do T7 falhou no CLI antes de chegar ao modelo e não conta como execução. Durante a rodada de validação, instalações externas e o repositório público não foram alterados.
