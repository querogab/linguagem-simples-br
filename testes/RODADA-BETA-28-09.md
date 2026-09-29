# Rodada comportamental da v0.6.0-beta.1

> Preparada em **28/09/26**. São **4 execuções**, sem linha de base nem micro-prompt: esta rodada valida correções do candidato, não sustenta comparação de superioridade.

> **Executada em 28/09/26** com quatro agentes isolados em `openai/gpt-5.6-sol`. Para contornar o cache da sessão principal, cada agente recebeu explicitamente o caminho do `SKILL.md`; portanto, a rodada validou comportamento, não descoberta automática. Resultados em [`resultados/2026-09-28__beta-comportamental/`](resultados/2026-09-28__beta-comportamental/).

## Pré-condições

- Reiniciar a ferramenta depois de sincronizar a skill. A sessão que estava aberta durante a cópia manteve o corpo anterior em cache.
- Confirmar na interface e registrar ferramenta, versão e modelo. Não inferir o modelo pelo texto da resposta.
- Usar um chat novo por caso, sem memória de outro caso.
- Candidato: `v0.6.0-beta.1`; SHA-256 do `SKILL.md`: `5C1374DD6181917C6E5BC38065B3DD2B6227177C723C95C8897E628ECF41617F`.
- Conferir que o corpo carregado contém a frase `A skill não avalia flexões neutras em texto privado.` Se aparecer a vedação geral antiga, parar: a ferramenta carregou a versão em cache.

## Execuções

### 1. C7: tabela verificável

Chamar a skill explicitamente e pedir:

```text
Revise o texto para o cidadão comum entender. Mostre a tabela completa antes/depois/por quê.

[cole testes/textos/T8__faq-esclarecimentos-pregao.txt]
```

**Aceite:** cada trecho original existe literalmente na entrada; cada trecho revisado existe literalmente na versão final; cada justificativa descreve a mudança real; nenhuma contagem é inventada; `poderá`, contraditório, ampla defesa e remissões permanecem; nenhuma resposta por remissão vira resposta categórica.

### 2. Texto privado com flexão neutra

Usar o prompt do eval 8 sem chamar a skill pelo nome, para conferir descoberta automática.

**Aceite:** não invoca a vedação do inciso XI para a empresa e não troca `Todes` apenas por ser flexão neutra.

### 3. Texto público com flexão neutra

Usar o prompt do eval 10 sem chamar a skill pelo nome.

**Aceite:** contextualiza o inciso XI no setor público, sem apresentar a flexão como vício técnico universal de linguagem simples.

### 4. Citação literal longa

Usar o prompt do eval 9 sem chamar a skill pelo nome.

**Aceite:** conteúdo entre aspas idêntico; explicação ou paráfrase fora das aspas.

## Registro

Salvar uma saída por execução em `testes/resultados/2026-09-28__beta-comportamental/`, com este cabeçalho:

```text
**Condição:** C7 | privado | público | citação
**Ferramenta e versão:**
**Modelo confirmado na interface:**
**Data:** DD/MM/AA
**Versão/hash da skill:** v0.6.0-beta.1 / 5C1374DD6181917C6E5BC38065B3DD2B6227177C723C95C8897E628ECF41617F
**Chat novo:** sim
```

Depois das quatro saídas, conferir os critérios sem usar o próprio modelo como avaliador. Reprovação em C7 bloqueia o formato completo; reprovação nos demais casos exige corrigir a instrução e repetir só o caso afetado.
