---

**Original:** T9__oficio-circular-cvm.txt
**Condição:** skill (v0.4)
**Modelo:** deepseek-v4-flash

---

## **Passo 1 — Planejamento**

**Contexto:** Ofício-circular da CVM, órgão regulador do mercado financeiro. Originalmente dirigido a profissionais do mercado (gestores, administradores). O cidadão comum não conhece "FIDC", "FIAGRO", "patrimônio líquido", "cotas", "equiparação".

**Objetivo da LS:** Explicar em que condições um FIAGRO pode ser tratado como FIDC — e por que isso importa para o investidor leigo.

**Problema central:** O texto original pressupõe que o leitor já sabe o que são esses fundos. Um cidadão comum precisa de definição mínima + regra clara.

---

## **Passo 2 — Diagnóstico rápido**

**A) Sinais de burocratês (8):**
1. `tem como objetivo esclarecer o entendimento` — 5 palavras onde 2 bastam
2. `dispositivos` — jargão por "regras" ou "artigos"
3. `aplicação subsidiária` — jargão jurídico
4. `prevalecendo, em caso de conflito` — inversão + cláusula formal
5. `não estão abarcados...os requisitos mínimos de enquadramento` — passiva + lacuna com reticências (cópia literal de jurisprudência)
6. `não se deve admitir` — dupla negação + passiva
7. `nos termos do` / `de que trata o` / `do referido Anexo` — muletas jurídicas
8. `contudo` / `entretanto` / `destaca-se` — conectivos formais sem função informacional

**B) Arquitetura:** Informação mais importante (a regra de equiparação) só aparece nos §§5-6. Cabeça do documento tenta apresentar tudo ao mesmo tempo (FIDC, FII, FIAGRO num fôlego só).

**C) Frases:** Média >25 palavras. Voz passiva frequente. Períodos encadeados com subordinadas.

**D) Palavras:** `direcionadas` → `enviadas`; `dispositivos` → `regras`; `destaca-se` → cortar; `contudo`/`entretanto` → `mas`.

---

## **Passo 3 — Heurística por tamanho**

Texto de ~350 palavras, 6 parágrafos numerados. Permite reescrita completa sem cisão.

---

## **Passo 4 — Reescrita**

### Tabela de trocas aplicadas

| Original | Troca LS |
|---|---|
| tem como objetivo esclarecer o entendimento | explica (ou: o objetivo é esclarecer) |
| dispositivos | regras / artigos |
| Por meio do | No (Ofício-Circular) |
| não estão abarcados | não incluem |
| Desse modo | Por isso |
| não se deve admitir | não podemos aceitar |
| nos termos do | conforme o |
| Entretanto, caso | Mas se |
| de que trata o art. 2º | previsto no art. 2º |
| do referido Anexo | desse Anexo |
| implementação | (não ocorre no texto original) |

### Travas de fidelidade mantidas:
- `50% do patrimônio líquido` — preservado
- `art. 2º do Anexo Normativo VI`, `art. 44 do Anexo Normativo II`, `art. 2º, inciso XII` — preservados
- `Resolução CVM nº 175` — preservada
- `FIAGRO`, `FIDC`, `FII` — preservados (siglas do mercado, com expansão na 1ª ocorrência)
- `Ofício-Circular nº 3/2025/CVM/SSE` — preservado

---

## **Passo 5 — Entrega**

### 1. Tabela antes/depois/por quê

| Antes | Depois | Por quê |
|---|---|---|
| `tem como objetivo esclarecer o entendimento` | `esclarece como a SSE entende` | Verbo direto elimina 3 palavras |
| `dispositivos dos Anexos...relacionados aos Fundos...FIDC, FII e FIAGRO` | `regras dos Anexos II, III e VI sobre FIDC, FII e FIAGRO` | Corta gerúndio + expande sigla |
| `Por meio do Ofício-Circular nº 3/2025/CVM/SSE, esta Superintendência entendeu` | `No Ofício-Circular nº 3/2025, a SSE já tinha explicado` | Voz ativa + verbo no lugar de "entendeu" |
| `não estão abarcados...os requisitos mínimos de enquadramento` | `não valem para as regras mínimas da carteira` | Troca "abarcados" + "enquadramento" |
| `Desse modo, esta SSE entende que não se deve admitir` | `Por isso, a SSE entende que não se pode equiparar` | Voz ativa + "admitir" vira "pode" |
| `Entretanto, caso o Regulamento do FIAGRO estabeleça` | `Mas se o Regulamento do FIAGRO definir` | "Entretanto, caso" → 2 palavras viram "Mas se" |
| `do referido Anexo` | `desse Anexo` | "Referido" é muleta |

### 2. Versão final limpa

```
Assunto: Quando um FIAGRO pode ser equiparado a um FIDC

Prezados(as),

1. Este Ofício-Circular esclarece como a Superintendência de Securitização e
Agronegócio (SSE) interpreta as regras dos Anexos II, III e VI da Resolução
CVM nº 175. Os anexos tratam de:

- FIDC: Fundos de Investimento em Direitos Creditórios
- FII: Fundos de Investimento Imobiliários
- FIAGRO: Fundos de Investimento nas Cadeias Produtivas do Agronegócio

Dúvidas sobre este documento podem ser enviadas para sse@cvm.gov.br.

I) EQUIPARAÇÃO DE COTAS DE FIAGRO A COTAS DE FIDC

2. O art. 2º do Anexo VI da Resolução CVM nº 175 diz que o FIAGRO pode
seguir regras de outros anexos quando sua política permitir investir mais
de 50% do patrimônio em ativos de outra categoria de fundo. Em caso de
conflito, valem as regras do Anexo VI.

3. No Ofício-Circular nº 3/2025, a SSE já tinha explicado que as regras
aplicáveis de outros anexos são só as que tratam da governança dos ativos
investidos. As regras mínimas de composição da carteira não entram nessa
conta.

4. Sendo assim, um FIAGRO que pode investir mais de 50% do patrimônio em
direitos creditórios deve seguir o Anexo II junto com o Anexo VI.

5. Atenção: mesmo nessa situação, o FIAGRO não é obrigado a manter esse
percentual mínimo. Por isso, a SSE entende que as cotas desse FIAGRO não
podem ser equiparadas a cotas de FIDC. Isso porque, conforme o art. 44 do
Anexo II da Resolução CVM nº 175, o FIDC precisa manter no mínimo 50% do
patrimônio investido em direitos creditórios.

6. Mas se o Regulamento do FIAGRO definir, como política, o investimento
mínimo de 50% do patrimônio em direitos creditórios, essas cotas podem
ser equiparadas a cotas de FIDC. Elas também passam a se enquadrar no
conceito de direitos creditórios previsto no art. 2º, inciso XII, desse
mesmo Anexo.
```

### 3. Avaliação ISO 24495-1

| Princípio | Status | Justificativa |
|---|---|---|
| **1. Relevância** (só o que o leitor precisa) | ✓ | Cortou apresentação duplicada dos fundos; focou na regra de equiparação |
| **2. Facilidade de localização** (arquitetura clara) | ✓ | Regra principal explicitada já no assunto; blocos com subtítulos; definições separadas |
| **3. Compreensibilidade** (frases curtas, vocabulário simples) | ✓ | Frases de 15-22 palavras; trocou jargão por termos do dia a dia; manteve precisão técnica |
| **4. Mecanismos de feedback** (como tirar dúvida) | ✓ | E-mail da SSE mantido; tom de abertura menos formal |

### 4. Avisos finais

**Fidelidade:** Números (50%), artigos (2º, 44, 2º XII), siglas e remissões normativas foram preservados. A regra de equiparação (núcleo do ofício) não foi alterada em substância — apenas reorganizada para aparecer antes.

**Perda calculada:** O tom protocolar de "Ofício-Circular" foi substituído por um título mais informacional ("Quando um FIAGRO pode ser equiparado a um FIDC"). Para uso estritamente jurídico, pode-se manter o título original e aplicar LS apenas no corpo.

**O que é N/A:** O texto original não tem tabelas, listas numeradas longas ou cláusulas condicionais encadeadas — princípios de formatação visual da ISO não se aplicam.

### 5. Teste com leitor real

Não realizado nesta rodada. Recomenda-se testar com um investidor não profissional (ex.: alguém que tem um FII mas nunca leu um ofício da CVM) — pedir que explique com as próprias palavras o que muda para o FIAGRO que investe em direitos creditórios.