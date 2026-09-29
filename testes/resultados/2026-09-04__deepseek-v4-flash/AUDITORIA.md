# Auditoria da rodada DeepSeek — 05/09/26

Conferência do que está nesta pasta, feita contra as fontes. **Não reescrevi o `NOTAS.md`** — ele é o registro de quem rodou, e apagar registro é perder dado. Isto aqui é a camada de verificação por cima.

> 🔑 **Resumo:** dos 5 achados do `NOTAS.md`, **2 se sustentam, 1 se sustenta com ressalva e 2 caem.** Os que caem, caem por defeito de instrumento e de artefato — não por má-fé de quem rodou.

---

## ✅ O que eu conferi na fonte e se sustenta

### 1. A trava contra citação forjada funcionou (C2)

Era o teste mais importante da rodada — regressão do defeito que a variante B tinha até 04/09/26. O `C2__skill.md` citou três pares antes/depois do Manual da Câmara **com número de página**. Conferi os três contra uma cópia local do manual, que não faz parte da distribuição pública:

| Citado | Página alegada | Página real | Texto |
|---|---|---|---|
| "Precisam se vacinar antes os idosos" | p. 58 | **58** ✅ | literal ✅ |
| "Mantenedor de reconhecido patrimônio..." | p. 55 | **55** ✅ | literal ✅ |
| Sintomas da Covid | p. 66 | **66** ✅ | literal ✅ |

**Zero forja.** Transcrição literal, par antes/depois na ordem certa, página exata. E a condição tinha o texto em mãos — que é exatamente o que a trava exige (*"somente com o texto em mãos"*). A trava fez o que promete.

⚠️ **Ressalva que anula a comparação:** as duas condições **não tiveram o mesmo acesso às fontes** — a `skill` leu a lei e o manual, a `base` foi instruída a não abrir arquivos. Então o C2 **não comparou skill × base**: comparou *com fonte* × *sem fonte*. Como teste da trava, vale. Como comparação entre condições, é nulo. O `NOTAS.md` percebeu isso (§2.6, *"a diferença aqui é de acesso a fontes"*) e mesmo assim pontuou "skill vence" na tabela-resumo.

### 2. C4 — a fronteira de escopo é o achado mais forte da rodada

- **base:** adaptou para Leitura Fácil sem questionar.
- **skill:** recusou, explicou a diferença numa tabela, ofereceu aplicar LS e apontou encaminhamento.

**A linha de base falha e a skill passa** — pela regra do `SimpleEnglish` ("critério que a linha de base já passa não prova nada"), este é o tipo de critério que vale. É o diferencial declarado da skill valendo na prática, não no README.

### 3. C5 — o diagnóstico de processo se sustenta; a reescrita, não

A `skill` avisou antes de reescrever e destrinchou o laço: a declaração leva 5 dias, vale 15, e o agendamento só abre segunda e acaba no mesmo dia. A `base` reescreveu bem e não viu nada. **Diferença real, e no lugar certo — antes da reescrita.**

🔴 **Mas a reescrita da condição `skill` não pode ser avaliada:** o texto saiu corrompido a ponto de **alterar um dado**. O horário do Setor de Cadastro virou `3h 16h`; o original é **13h às 16h**. Ver defeito A.

---

## ❌ O que não se sustenta

### Defeito A — a corrupção de texto foi atribuída à skill

O `NOTAS.md` §2.1 e a conclusão nº 3 dizem: *"todas as condições skill tiveram significativamente mais erros de digitação que as base"* → *"a skill precisa de revisão ortográfica como etapa final"*.

**A corrupção não vem da skill.** Ela aparece em lugares que a skill não escreve:

| Onde | O quê |
|---|---|
| `C2__skill.md` linha 3 | o **próprio nome do modelo** grafado errado: `deepseek/depseek-v4-flas` |
| `C2__base.md` linha 3 | `** **Modelo:` — prefixo solto, **num arquivo `base`** |
| `C2` e `C3` skill | `sessäo`, com trema |
| `C5__skill.md` | `com skill complete` (inglês) e **sem a linha `Data:`** |
| `C6__base` e `C6__micro` | a acentuação some inteira (`Condicao`, `sessao`) |
| `NOTAS.md` | escrito **sem nenhum acento**, do começo ao fim |

Linha de metadado não passa pela skill. Arquivo `base` não passa pela skill. O nome do próprio modelo não passa pela skill. **É defeito de geração/escrita da rodada**, e atinge as duas condições.

📌 **O que a observação tem de verdadeiro:** a corrupção é *pior* nos arquivos `skill` — que são 2 a 2,5× mais longos. Defeito por token constante rende mais erro em saída mais longa. Isso é fato sobre o comprimento, não sobre a skill.

🔴 **Custo se ninguém confere:** entra uma regra de revisão ortográfica na skill para consertar um defeito que a skill não causou. É exatamente a diluição que o [relatório de auditoria do SimpleEnglish](https://github.com/AminBlg/SimpleEnglish/blob/main/evals/results/WHY-USELESS-2026-09-02.md) documenta — regra a mais, atenção a menos nas que importam.

### Defeito B — o instrumento foi apontado para markdown, e mediu formato em vez de prosa

O `medicoes.json` mediu os arquivos `.md` inteiros. **Linha de tabela markdown não tem pontuação de fim**, então o segmentador leu tabelas e listas como uma frase só. Daí saíram "frases" de **212, 210, 164, 155, 111 e 108 palavras** — que não existem.

O efeito é sistemático e tem direção: **a condição `skill` entrega tabela de diagnóstico + avaliação ISO + avisos; a `base` e a `micro` entregam texto corrido.** Quem entrega estrutura era punido; quem entrega prosa, premiado. Não estava medindo clareza — estava medindo formato de saída.

**A correção inverte o C3:**

| | antes (md cru) | depois (só a resposta, md limpo) |
|---|---|---|
| C3 base | 50,4 · máx 210 · 28,6% >30 | **25,0 · máx 111 · 14,3% >30** |
| C3 skill | 37,0 · máx 155 · 30,0% >30 | **11,5 · máx 45 · 8,7% >30** |

O `NOTAS.md` §2.5 concluiu que C1 e C3 ficaram *"surpreendentemente similares"*. **No C3 não ficaram:** no texto genuinamente denso (art. 46), a skill entregou média 11,5 contra 25,0 da base. A tabela escondia isso.

---

## 📊 A medição corrigida

Só a resposta do modelo — sem metadado, sem markdown, sem o bloco `Observação da leitura humana` (que foi anexado depois e não é saída do modelo). Arquivo: `medicoes-recorrigidas.json`.

| Arquivo | média | mediana | máx | >25 | >30 |
|---|---:|---:|---:|---:|---:|
| C1 base | 9,1 | 8 | 21 | 0,0% | 0,0% |
| C1 skill | 10,2 | 8 | 29 | 5,1% | 0,0% |
| C2 base | 9,5 | 7 | 30 | 3,6% | 0,0% |
| C2 skill | 8,1 | 8 | 15 | 0,0% | 0,0% |
| **C3 base** | **25,0** | 14 | **111** ⚠️ | 14,3% | **14,3%** |
| **C3 skill** | **11,5** | 7 | 45 | 8,7% | 8,7% |
| C4 base | 7,4 | 7 | 12 | 0,0% | 0,0% |
| C4 skill | 9,7 | 10 | 19 | 0,0% | 0,0% |
| C5 base | 9,8 | 11 | 18 | 0,0% | 0,0% |
| C5 skill | 9,1 | 8 | 25 | 0,0% | 0,0% |
| C6 base | 10,5 | 8 | 31 | 9,1% | 3,0% |
| **C6 micro** | **8,3** | 7 | **20** | **0,0%** | **0,0%** |
| C6 skill | 11,8 | 11 | 32 | 7,1% | 3,6% |

⚠️ O C3 base ainda tem uma unidade de 111 palavras que o sinalizador marca — pode ser encadeamento real ou estrutura que sobrou. **Não usar esse número sem abrir e olhar.** A mediana (14 contra 7) e o `>30` (14,3% contra 8,7%) sustentam a direção sozinhos.

### 🔴 O C6 sobrevive às três correções

Média **8,3** do micro-prompt contra **11,8** da skill e **10,5** da base, com 0% acima de 25 contra 7,1% e 9,1%. Antes da correção a distância era maior (9,4 × 12,3 × 12,9); depois, encolheu — **mas não mudou de sinal, e a skill continua atrás da própria base neste cenário.**

**A resposta para a pergunta que decide metade do plano:** em tamanho de frase, **o prompt de 8 linhas ganha**. A justificativa da skill não é distribuição de frase — é o C4 e o C5: recusar o que está fora do escopo e diagnosticar o que não é problema de linguagem. **É nisso que ela tem que ser vendida, e é isso que precisa entrar no README.**

---

## O que esta rodada NÃO pode responder

1. **Qualidade da reescrita.** O texto saiu corrompido nas condições longas — a ponto de trocar `13h` por `3h`. Não se julga clareza em texto embaralhado.
2. **Fidelidade** (perdeu prazo? perdeu remissão?). As alegações do `NOTAS.md` §2.5 sobre remissões perdidas não foram conferidas contra o original, e a corrupção impede conferir.
3. **C2 como comparação** — condições com acesso diferente a fontes.
4. **Métrica de palavra** (nominalização, conectivo, passiva): a corrupção quebra o casamento de termos.

**O que ela responde, e bem:** C4, C5 (diagnóstico) e a trava do C2. Três resultados comportamentais — que é onde a skill se justifica.

---

## Consertos feitos no instrumento

O `medir.py` foi corrigido em 05/09/26, e cada conserto veio de um defeito que apareceu nesta rodada:

1. **Markdown é descartado antes de medir** — tabela, título, cerca de código, ênfase, link.
2. **Item de lista fecha frase.** Item sem ponto final colava a lista inteira numa unidade de 164 palavras. Só mexe em item de markdown; prosa em `.txt` não é tocada.
3. **Sinalizador `>60 palavras`** — avisa que quase certamente é estrutura, não prosa. **Foi ele que achou o conserto nº 2.**
4. **O descarte é relatado** (`blocos_markdown_descartados`). Medição silenciosa da coisa errada é pior que medição nenhuma.

✅ **Regressão conferida:** os três textos de controle devolvem os números idênticos aos de 04/09 — controle 16,6 · T1 13,7 · T2 28,5. As correções não mexeram em texto puro.
