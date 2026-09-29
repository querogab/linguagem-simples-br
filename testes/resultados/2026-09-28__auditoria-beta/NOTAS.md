# Auditoria da beta — 28/09/26

**Objeto:** resultados T5–T9 da v0.5.1, usados como matéria-prima para os exemplos da beta.
**Método:** conferir tabela e versão final contra a entrada original. Esta é uma auditoria documental, sem nova execução de modelo.

## C7 — tabela antes/depois

**Resultado: reprovado na v0.5.1.** As tabelas descrevem mudanças que em geral ocorreram, mas trazem contagens não verificadas. A saída do FAQ também introduz respostas que não estavam no original.

| Caso | Conferência | Uso na beta |
|---|---|---|
| T5, BNCC | O original e a reescrita existem. A tabela chama a competência 1 de "58 palavras" e diz que virou "2 frases (26 + 22)"; o original tem 31 palavras e a versão final tem 3 frases. | Exemplo usa apenas a abertura, sem as contagens inventadas. |
| T6, MCASP | A transformação para lista ocorreu. As contagens "35" e "60+" não foram produzidas por instrumento nem conferidas na entrega. | Exemplo mostra a regra transformada em lista, sem alegar contagem. |
| T7, edital UECE | A abertura foi reestruturada, mas a tabela afirma "85 palavras" sem contagem documentada. A versão também infere "Podem participar estudantes de graduação" a partir do programa e da seleção, não de uma regra de elegibilidade no trecho. | Exemplo usa um objetivo do programa, sem a inferência da abertura. |
| T8, FAQ MDH | A pergunta 2 dizia que a infração "poderá" impedir a contratação; a saída abre com "Sim". A pergunta 3 remetia ao anexo; a saída inventa uma resposta direta e categórica. | Essas respostas ficam excluídas. Exemplo usa a pergunta 4 e preserva a remissão oficial. |
| T9, ofício CVM | Os trechos conferidos existem e as condições de 50%, remissões e modalidade permanecem. | Exemplo usa a explicação do art. 2º e mantém as três condições. |

## Correção no candidato

A v0.6.0-beta.1 ganhou uma conferência operável para cada linha da tabela: trecho original e revisado literais, motivo correspondente, contagem só quando feita e proibição de transformar inferência em fato. Isso corrige a instrução, mas **a eficácia ainda precisa de nova execução** antes de alegar que C7 passou no candidato.

## Comportamentos alterados

Conferência estática do arquivo:

- texto privado com flexão neutra: a skill declara que não avalia por esse motivo;
- texto público: o inciso XI aparece como regra legal contextual, fora dos anti-padrões técnicos;
- citação literal longa: a skill manda manter as aspas e simplificar a explicação ao redor;
- apêndice legal: link relativo dentro do pacote instalável;
- justificativa falsa dos 16/18: retirada dos trechos vivos do produto.

Esses itens precisam de execução comportamental para passar; leitura do arquivo confirma apenas que a instrução foi corrigida.

## Empacotamento local

- o delta da v0.5.1 foi aplicado sobre a v0.5 e reconstruiu o SHA-256 registrado;
- os oito arquivos do pacote foram copiados para uma pasta temporária limpa e ficaram idênticos à fonte;
- UTF-8, frontmatter, nome da pasta e links relativos passaram na checagem local;
- a especificação vigente do Agent Skills foi conferida em `https://agentskills.io/specification`;
- a cópia instalada nesta raiz está em sincronia, mas a sessão aberta antes da atualização devolveu o corpo antigo em cache. O carregamento da beta precisa ser repetido após reiniciar a ferramenta.
