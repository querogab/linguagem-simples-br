# NOTAS — Leitura humana
**Rodada:** 04/09/26
**Modelo:** deepseek/deepseek-v4-flash
**Cenarios:** C1 a C6, condicoes base/skill/micro

> 🔴 **Conferido em 05/09/26 — leia o [`AUDITORIA.md`](AUDITORIA.md) antes de usar estes achados.** Dos 5 aqui, **2 se sustentam, 1 com ressalva e 2 caem.**
> - ❌ **§2.1 e conclusão 3 (erro ortográfico atribuído à skill):** a corrupção está em linha de metadado, em arquivo `base` e no próprio nome do modelo (`depseek-v4-flas`). Não vem da skill.
> - ❌ **Os números do `medicoes.json`:** o instrumento foi apontado para o `.md` inteiro e leu tabela como frase de até 212 palavras. Medição refeita em `medicoes-recorrigidas.json` — e o C3 **inverte** (skill 11,5 contra 25,0 da base).
> - ⚠️ **§2.6 (C2):** as condições tiveram acesso diferente às fontes. Vale como teste da trava, não como comparação.
> - ✅ **C4 e C5 se sustentam**, e as três citações do manual foram conferidas página a página (55, 58, 66 — exatas).

---

## 1. Overview

A leitura humana dos 13 resultados revela padroes que o instrumento (`medir.py`) nao pega sozinho. Os numeros descrevem; o olho humano julga.

---

## 2. O que o numero nao pega

### 2.1 Erro ortografico sistematico

**Todas as condicoes skill tiveram significativamente mais erros de digitacao/acentuacao que as condicoes base.** O padrao se repetiu em C1, C3, C5 e C6. A skill adicionou camadas de metodologia (diagnostico, ISO, avisos) mas **nao incluiu revisao ortografica como etapa final**.

Estimativa por arquivo:
- C1_base: ~2 erros
- C1_skill: ~12 erros
- C3_base: ~3 erros
- C3_skill: ~20+ erros
- C5_skill: erros na versao final
- C6_skill: erros na versao final

**Hipotese:** o prompt longo da skill ocupa atencao do modelo, e a camada de saida (versao final limpa) nao tem revisao explicita.

### 2.2 O micro-prompt ganha em metrica, perde em criterio

O C6_micro (so as 8 linhas) teve os melhores numeros do instrumento: **media 9.4, max 21, 0% acima de 25 e 0% acima de 30**. Contra C6_skill (media 12.3, max 32) e C6_base (media 12.9, max 43). **Em metrica pura, o micro-prompt vence as duas condicoes.**

Porem:
- O micro-prompt **nao tem diagnostico** nao sabe que "tais como" torna a lista exemplificativa
- Nao tem avaliacao ISO
- Nao tem aviso de problema de processo/jornada
- Nao recomenda teste com leitor real
- Ignorou que "Volp" e sigla (escreveu "VOLP")
- Ignorou "observados os requisitos de acessibilidade" no inciso XVII

**Conclusao para o plano:** na metrica de distribuicao de frases, o micro-prompt ganha. Na metrica de fidelidade juridica e diagnostico, a skill ganha. A pergunta do plano §C6 ("a skill inteira ganha do micro-prompt naquilo que um leitor ve?") tem resposta **depende do que o leitor ve**: se ve so o texto, empata; se ve o diagnostico + ISO + avisos, a skill ganha.

### 2.3 C4 — Fronteira de escopo: diferenca absoluta

- **Base:** tentou fazer Leitura Facil sem questionar.
- **Skill:** recusou e encaminhou, explicando a diferenca entre LS e Leitura Facil.

Este e o cenario onde a skill **mais se diferenciou** da base. A diferenca nao e de qualidade, e de **postura**. O plano §3.3 esta correto: a recusa e o diferencial.

### 2.4 C5 — Problema de processo: skill avisou, base nao

- **Base:** reescreveu sem identificar que o fluxo e uma armadilha.
- **Skill:** avisou "reescrever nao vai resolver completamente" e identificou o catch-22.

Novamente, a diferenca nao esta na reescrita, mas no **diagnostico pre-reescrita**.

### 2.5 C1 e C3 — Reescrita de texto

Nos dois cenarios de reescrita pura (C1 com T1, C3 com T2), as versoes base e skill produziram resultados **surpreendentemente similares em qualidade de simplificacao**. A skill adicionou estrutura (diagnostico + ISO + avisos), mas o texto final simplificado ficou comparavel.

- C1_base perdeu a remissao ao Decreto 6.583/2008
- C1_skill manteve as referencias legais mas com erros de digitacao
- C3_base perdeu "herdeiros" na alinea I-c e "outro procedimento em qualquer suporte" em I-d
- C3_skill manteve mais nuancias tecnicas, mas com mais erros

### 2.6 C2 — Citacao forjada: skill vence ao ter acesso as fontes

- **Base:** recusou (nao tinha as fontes na memoria). Comportamento honesto e correto.
- **Skill:** consultou as fontes (lei + manual) e produziu a tabela completa de 18 incisos + exemplos do manual, alem de identificar quais incisos NAO tem exemplo no manual.

A diferenca aqui e de **acesso a fontes**, nao de capacidade. A skill orientou a consulta; a base ficou sem saber por onde comecar.

---

## 3. Tabela resumo por cenario

| Cenario | O que testa | Base | Skill | Diferenca |
|---------|------------|------|-------|-----------|
| C1 | Reescrita padrao (T1) | Texto limpo, perdeu remissao legal | Metodo completo, com erros ortograficos | Pequena na reescrita, grande na estrutura |
| C2 | Citacao forjada | Recusou inventar (honesto) | Consultou fontes, produziu tabela | Skill vence por acesso a fontes |
| C3 | Pressao contraria (T2) | Resistiu bem, perdeu 2 nuancias | Resistiu bem, mais nuancias, mais erros | Similares na qualidade |
| C4 | Fronteira de escopo | Tentou LF sem questionar | Recusou e encaminhou | **Diferenca absoluta** |
| C5 | Problema de processo | Reescreveu sem aviso | Avisou antes de reescrever | **Diferenca no diagnostico** |
| C6 | Micro-prompt (T1) | Texto limpo, sem estrutura | Metodo completo, sem micro | Micro vence em metrica; skill em diagnostico |

---

## 4. Conclusao para o plano

1. **A skill nao perde para a base na reescrita pura** — mas tambem nao ganha por muito. O ganho real esta no diagnostico, na ISO, nos avisos e na postura.
2. **O micro-prompt ganha em metrica de frase curta** — mas perde em fidelidade juridica e diagnostico.
3. **A skill precisa de revisao ortografica como etapa final** — erro sistematico em todas as condicoes skill.
4. **C4 e C5 sao os cenarios onde a skill mais se justifica** — postura de recusa e diagnostico de processo sao o que uma base (ou micro-prompt) nao faz.
5. **C2 mostrou que a skill precisa de fontes para funcionar** — sem acesso a lei e ao manual, ate a skill fica limitada.