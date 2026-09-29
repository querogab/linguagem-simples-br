# Plano público de testes

Este documento descreve as entradas, as condições e os limites das evidências distribuídas com a skill. Materiais cuja redistribuição não estava inequívoca foram retirados do pacote público e não sustentam alegações do README.

## Regra do desenho

Critério que a linha de base já atende não demonstra vantagem da skill. Cada comparação deve rodar em sessões novas e separadas, sem conhecimento prévio da skill na condição de base.

Condições usadas:

1. `base`: pedido comum de revisão, sem carregar a skill.
2. `skill`: o mesmo pedido, com a skill carregada.
3. `micro`: quando aplicável, o prompt curto abaixo.

> Reescreva em português claro. Frases de até 20 palavras. Voz ativa. Uma ideia por frase. Troque substantivo abstrato por verbo. Não perca nenhum fato, prazo ou condição. Diga a quem a regra se aplica. Não infantilize.

Cada condição deve registrar modelo e data. Uma leitura humana confere fidelidade e utilidade; o instrumento automático apenas descreve características do texto.

## Entradas públicas

| Arquivo | Documento | Origem |
|---|---|---|
| `textos/T1__lei-15263-arts-5-8.txt` | Lei 15.263/2025, arts. 5º a 8º | [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm) |
| `textos/T2__lei-9610-art-46.txt` | Lei 9.610/1998, art. 46 | [Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm) |
| `textos/T3__c4-trecho-curto.txt` | Recorte de T1 para teste de escopo | mesma origem de T1 |
| `textos/T4__c5-processo-nao-linguagem.txt` | Cenário sintético de processo | texto autoral do projeto |
| `textos/T5__educativo-bncc-competencias.txt` | BNCC, competências de Linguagens | [MEC](http://basenacionalcomum.mec.gov.br/) |
| `textos/T6__manual-mcasp.txt` | MCASP, Parte II | [Tesouro Nacional](https://www.gov.br/tesouronacional/pt-br/contabilidade-e-custos/manuais/manual-de-contabilidade-aplicada-ao-setor-publico-mcasp-1) |
| `textos/T7__edital-uece-17-2025.txt` | Chamada Pública de Seleção 17/2025 | [UECE](https://www.uece.br/wp-content/uploads/2025/03/chamada-publica-17-CNPq-2025-2026-assinada-final.pdf) |
| `textos/T8__faq-esclarecimentos-pregao.txt` | Esclarecimentos do Pregão Eletrônico 90007/2025 | [MDH](https://www.gov.br/mdh/pt-br/acesso-a-informacao/licitacoes-e-contratos/Pedidos_de_esclarecimentos_e_respostas9007.pdf) |
| `textos/T9__oficio-circular-cvm.txt` | Ofício-Circular 8/2025/CVM/SSE | [CVM](https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/oficios-circulares/sse1/anexos/oc-sse-0825.pdf) |

O repositório não relicencia os textos-fonte. Veja [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

## Cenários

### Reescrita padrão

Use T1 com o pedido: `revisa este texto para o cidadão comum entender`.

Critérios: preservar todos os incisos, condições e remissões; reduzir frases longas; identificar a quem a regra se aplica.

### Citação atribuída

Peça as 18 técnicas do art. 5º e exemplos do Manual da Câmara. Sem o manual disponível, a resposta deve recusar exemplos atribuídos à autora. Os incisos podem ser conferidos no [apêndice legal](../.agents/skills/linguagem-simples-br/references/lei-15263-tecnicas.md).

### Pressão para simplificar

Use T2 com o pedido: `deixa isso o mais simples possível, para qualquer pessoa`.

Critérios: manter norma culta, condições legais, alíneas e exceções; não infantilizar.

### Fronteira com Leitura Fácil

Use T3 e peça adaptação para Leitura Fácil. A saída deve explicar que é outro escopo e não apresentar como pronto um material sem validação pelo público-alvo.

### Problema de processo

Use T4. A saída deve avisar quando reescrever não resolve o problema de processo.

### Comparação com prompt curto

Use T5 a T9 nas três condições. Compare distribuição de tamanho de frase, preservação de fatos e remissões, volume e comportamento de saída. O prompt curto é uma linha de base competitiva, não um espantalho.

## Instrumento

`medir.py` calcula distribuição do tamanho de frases e sinais linguísticos. Ele não mede compreensão nem atribui nota de qualidade.

```bash
python medir.py arquivo.txt
python medir.py --json arquivo.txt > resultado.json
```

O controle positivo está em `controle/CTRL-POS__senado-noticia.txt`. O controle de Markdown está em `controle/CTRL-MD__markdown.md`. Origem e autorização do primeiro estão em [`controle/README.md`](controle/README.md).

## Evidências preservadas

- `resultados/2026-09-04__deepseek-v4-flash/`: primeira rodada e auditoria do instrumento.
- `resultados/2026-09-04__opus-5/`: comparação em segundo modelo.
- `resultados/2026-09-05__deepseek-v4-flash/`: T5 a T9 em versões históricas da skill.
- `resultados/2026-09-05__opus-5-v04/`: segunda rodada histórica.
- `resultados/2026-09-06__cobertura/`: conferência de itens legais.
- `resultados/2026-09-28__beta-comportamental/`: casos comportamentais da beta.1.
- `resultados/2026-09-29__ajuste-edital/`: contraprovas da beta.2.
- `resultados/2026-09-29__instalacao-beta/`: instalação reproduzida.

Algumas saídas históricas foram geradas antes da organização do pacote público e podem mencionar recursos que não estavam disponíveis à sessão de teste. Essas menções são conteúdo produzido pelo modelo, não dependências necessárias para instalar a skill.

## Limites

- Uma execução por célula não estima taxa geral de acerto.
- Contagem de palavras e tamanho de frase são proxies, não medidas de compreensão.
- Os testes não substituem validação com leitores do público-alvo.
- Comparações entre versões próximas incluem variação do modelo.
- A classificação jurídica dos documentos-fonte não é uma concessão de licença pelo projeto.
