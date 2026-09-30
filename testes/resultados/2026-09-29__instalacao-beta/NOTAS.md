# Teste de instalação da v0.6.0-beta.1

> Este primeiro bloco registra a beta.1. A repetição da beta.2 está no fim do arquivo.

**Data:** 29/09/26  
**Ferramenta:** OpenCode `1.18.33`  
**Modelo:** `openai/gpt-5.6-sol`  
**Candidato:** `v0.6.0-beta.1`  
**SHA-256 do `SKILL.md`:** `5C1374DD6181917C6E5BC38065B3DD2B6227177C723C95C8897E628ECF41617F`

## Ambiente

O pacote de oito arquivos foi copiado para `.opencode/skills/linguagem-simples-br/` em um projeto temporário sem arquivos da raiz de trabalho. A conferência byte a byte passou. Em processo novo, `opencode debug skill` encontrou o candidato. A descoberta continuou funcionando com a leitura de skills externas desativada, o que isolou a cópia do projeto.

## Resultados

| Caso | A skill carregou? | Resultado |
|---|---:|---|
| Chamada explícita + recursos locais | sim | Leu `references/lei-15263-tecnicas.md`, os cinco arquivos de `exemplos/` e devolveu corretamente o inciso XI. |
| Descoberta por pedido de revisão | sim | Revisou o e-mail privado de ponta a ponta. Preservou `deverá`, `poderemos`, o prazo de até cinco dias úteis, a condição de recebimento integral e a ausência de aprovação. |
| Descoberta por pedido de simplificação | sim | A skill carregou e entregou o formato completo para texto público. A entrada chegou com as aspas corrompidas pelo transporte do argumento no CLI do Windows; a saída preservou essa entrada. O caso prova descoberta, mas não conta como teste de fidelidade da citação. |
| Pedido fora do escopo | não | Respondeu `391` a `17 vezes 23`, sem chamar a skill. |

## Defeito do harness

O prompt do terceiro caso continha uma citação entre aspas duplas. O export da sessão mostrou que o CLI recebeu `A" administração ... "pedido`, em vez da entrada preparada. A resposta sinalizou as aspas deslocadas e manteve o texto recebido. Não houve quinta execução: a preservação de citação já tinha passado na rodada comportamental de 28/09/26, e o fluxo completo foi exercitado no e-mail privado desta rodada.

## Veredito

A instalação local no OpenCode passou em chamada explícita, descoberta automática por dois gatilhos, acesso aos recursos, fluxo completo e não disparo fora do escopo. A evidência cobre uma ferramenta, um modelo e uma execução por caso. Claude Code e outras ferramentas permanecem como compatibilidade esperada pelo formato, não como instalação reproduzida nesta beta.

## Contraprova pela URL pública

Depois da publicação, o repositório `https://github.com/querogab/linguagem-simples-br` foi clonado em outra pasta temporária. O primeiro clone expôs conversão de LF para CRLF no Windows: o conteúdo era o mesmo, mas o hash mudou. O repositório ganhou `.gitattributes` com `eol=lf`, e a contraprova foi repetida do zero.

No segundo clone, o `SKILL.md` voltou ao SHA-256 esperado (`5C1374...`). A pasta baixada foi copiada para `.opencode/skills/` em outro projeto vazio; `opencode debug skill`, com skills externas desativadas, encontrou `linguagem-simples-br`. O exemplo `01-bncc-abertura.md` também abriu pelo pacote clonado, com fonte e vínculo ao resultado bruto.

## Repetição com a v0.6.0-beta.2

Depois da publicação da beta.2, a instalação foi repetida pela URL pública com:

```bash
npx skills add querogab/linguagem-simples-br --agent opencode --copy -y
```

O pacote publicado tinha oito arquivos. O `SKILL.md` instalado reproduziu o SHA-256 `4BAD6E6AFACD1EFE8F0F86827F95D736B3C54D39282FD80238F8EAE10D5BDBC3`, e o OpenCode `1.18.33` carregou a cópia instalada em processo novo.

Esta primeira evidência não cobre as correções de auditoria posteriores, que acrescentaram avisos e o texto da licença ao pacote. Por isso, a instalação foi repetida na contraprova abaixo.

## Instalação pública da v0.6.0-beta.3

- **Data:** 30/09/26
- **Ferramenta:** OpenCode `1.18.33`
- **Candidato:** `v0.6.0-beta.3`
- **SHA-256 do `SKILL.md`:** `A3A546AF8B54F28DBEE69B29D1D6E089378F2221894AE686685FBEEB05C5C58F`

Depois da reescrita do `main`, a instalação pela URL pública foi repetida com o mesmo comando. O instalador encontrou uma skill e copiou 10 arquivos para `.agents/skills/linguagem-simples-br/` num projeto temporário limpo.

A comparação por caminho e SHA-256 confirmou igualdade byte a byte entre os 10 arquivos instalados e a fonte pública local. Com as skills externas do Claude Code desativadas, `opencode debug skill` carregou `linguagem-simples-br` a partir da pasta temporária e mostrou a versão `0.6.0-beta.3`.

Não houve chamada de modelo nesta contraprova. Ela verifica descoberta, cópia, integridade e carregamento do pacote; os casos comportamentais permanecem nas rodadas próprias.
