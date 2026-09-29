# Controles do medidor

Estes dois arquivos conferem o `medir.py`, não a skill. Nenhuma condição de teste revisa nenhum deles.

| Arquivo | O que confere | Valor esperado |
|---|---|---|
| `CTRL-POS__senado-noticia.txt` | Controle positivo. É prosa jornalística, e o instrumento tem que mostrá-la como o texto mais limpo dos três. | média 16,6 · mediana 18 · máximo 29 palavras por frase |
| `CTRL-MD__markdown.md` | Controle de markdown. Tem tabela, título, cerca de código, listas e link em volta de 7 frases de prosa com tamanho conhecido. | 7 frases · 88 palavras · média 12,6 · mediana 8 · máximo 34 |

Para rodar, a partir da pasta `testes/`:

```bash
python medir.py controle/CTRL-POS__senado-noticia.txt textos/T1__lei-15263-arts-5-8.txt textos/T2__lei-9610-art-46.txt
python medir.py controle/CTRL-MD__markdown.md
```

A primeira linha deve devolver 16,6/18/29 para o controle, 13,7/11/49 para o T1 e 28,5/32/58 para o T2. Se o controle não sair assim, o instrumento mudou. O [plano de testes](../plano-de-testes.md) registra quando cada valor foi fixado.

## De onde vem o texto do Senado

É um trecho da matéria *"Linguagem simples em mensagens de órgãos públicos agora é obrigatória"*, da **Agência Senado**, publicada em 17/11/2025 e atualizada em 18/11/2025. A matéria não traz autor individual; a assinatura é da própria agência.

Matéria completa: https://www12.senado.leg.br/noticias/materias/2025/11/17/linguagem-simples-em-mensagens-de-orgaos-publicos-agora-e-obrigatoria

**Este arquivo não está sob a licença MIT do repositório.** A [política de uso da Agência Senado](https://www12.senado.leg.br/noticias/politica-de-uso), conferida em 29/09/26, diz: *"A reprodução de matérias e fotografias é livre, desde que não haja descaracterização de conteúdo e mediante a citação da Agência Senado e do autor."*

Essa autorização basta aqui porque o texto só é reproduzido e medido. Ele não é usado como entrada de reescrita. Os demais limites de licença estão em [`../../THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md).

**O arquivo guarda o trecho exatamente como foi extraído em 04/09/26.** Cobre cerca de três quartos do corpo da matéria, que tem umas 350 palavras. No início ficaram o título da página e duas linhas de seletores de estilo, sobras da extração. Ninguém limpou essas sobras, e isso foi intencional: os valores de referência do controle dependem destes bytes, e limpar o arquivo mudaria o instrumento. Para ler a matéria inteira, use o link acima.
