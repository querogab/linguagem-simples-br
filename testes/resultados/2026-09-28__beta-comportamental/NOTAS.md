# Validação comportamental da v0.6.0-beta.1

**Data:** 28/09/26. **Modelo:** `openai/gpt-5.6-sol`. **Desenho:** quatro agentes isolados, uma execução por caso, lendo diretamente o `SKILL.md` canônico com SHA-256 `5C1374DD6181917C6E5BC38065B3DD2B6227177C723C95C8897E628ECF41617F`.

## Resultado

| Caso | Resultado | Evidência |
|---|---|---|
| C7: tabela verificável | **Passou** | 8 de 8 células da coluna original existem literalmente na entrada; 8 de 8 células revisadas existem na versão final; justificativas correspondem às mudanças; nenhuma contagem foi alegada; modalidade, contraditório, ampla defesa, condições e remissões foram preservados. |
| Flexão neutra em texto privado | **Passou** | `Todes` permaneceu intacto e a vedação pública não foi invocada. |
| Flexão neutra em texto público | **Passou com ressalva de apresentação** | A saída aplicou o inciso XI apenas à prefeitura e distinguiu o contexto público. Porém, colocou o achado na categoria `[D]`, usada para problema de palavra; seria mais preciso apresentá-lo somente como aviso legal contextual. |
| Citação literal longa | **Passou** | O conteúdo entre aspas permaneceu idêntico; a explicação veio fora das aspas. |

## Ressalvas do C7

- A saída expandiu `MTE/SIT` com conhecimento do modelo. As expansões estão corretas, mas não vieram da entrada. Isso não alterou regra, condição ou modalidade; ainda assim, texto real precisa de validação técnica.
- A frase final diz que a versão preserva “datas”, embora a entrada não traga data-calendário. É uma afirmação genérica desnecessária, não uma linha inventada na tabela.

As duas ressalvas não atingem o critério de reprovação definido antes da rodada. Não houve resposta por remissão transformada em resposta categórica, contagem inventada ou mudança inexistente descrita pela tabela.

## Limites

- Uma execução por caso e um único modelo. O resultado permite afirmar apenas que estes quatro casos passaram nesta rodada.
- Os agentes receberam o caminho da skill explicitamente. A rodada valida comportamento, não descoberta automática nem recarga da instalação.
- Nenhum leitor do público-alvo participou.
