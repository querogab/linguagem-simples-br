# Contraprova do eval 11

**Data:** 29/09/26  
**Ferramenta:** OpenCode `1.18.33`  
**Modelo:** `openai/gpt-5.6-sol`  
**Ambiente:** projeto temporário, cópia ajustada em `.opencode/skills/`, skills externas desativadas  
**Prompt:** `Revise este trecho de edital sem alterar a numeração nem inventar informação: 3.2 O candidato/a deverá entregar estas no prazo de 5 dias.`

## Saída integral

> **Versão revisada**
>
> 3.2 A pessoa candidata deverá entregá-las no prazo de 5 dias.
>
> **Aviso:** “estas” não tem referente no trecho enviado. A versão pressupõe que o item anterior menciona palavras no feminino plural. Confirme esse referente antes de publicar.
>
> Fiz 2 mudanças: retirei a barra de gênero e substituí “estas” por “entregá-las”. A numeração, a obrigação e o prazo foram preservados.

## Veredito

| Critério | Resultado |
|---|---|
| preservar `3.2` | passou |
| preservar `deverá` e `5 dias` | passou |
| tratar a barra sem confundir com flexão neutra | passou |
| identificar a ambiguidade sem inventar referente | **reprovou** |

O modelo diagnosticou corretamente que `estas` não tinha referente, mas entregou `entregá-las` como se o objeto fosse conhecido. A regra foi endurecida depois da execução: sem referente recuperável, a versão provisória deve usar `[referente a confirmar]` ou aguardar esclarecimento. Naquele ponto, a correção ainda precisava de reexecução; o resultado dela está abaixo.

## Reexecução depois da correção

> **Antes e depois**
>
> | Trecho original | Versão revisada | Motivo |
> |---|---|---|
> | “O candidato/a” | “A pessoa candidata” | Retira a barra de gênero e melhora a leitura. |
> | “estas” | “[referente a confirmar]” | O texto não informa o que deve ser entregue. |
>
> **Versão revisada**
>
> 3.2 A pessoa candidata deverá entregar [referente a confirmar] no prazo de 5 dias.

A saída preservou `3.2`, `deverá` e `5 dias`; tratou a barra sem mencionar flexão neutra; e não inventou o objeto. Também avisou que o trecho não informa quando começa a contagem dos cinco dias. Esse aviso não acrescentou informação à versão revisada.

**Veredito da reexecução: passou nos quatro critérios.** Uma execução por estado do artefato não estabelece taxa de acerto; apenas confirma que a trava nova operou neste caso.
