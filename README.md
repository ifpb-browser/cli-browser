cli-browser
===========

Navegador web de linha de comando.

Execução
--------

```
pip install -e .
python -m cli_browser
```

Comandos
--------

Toda entrada é digitada no prompt `url:`. Comandos começam com `#`, e os que
recebem uma url exigem um espaço antes dela, portanto `#addwww.ifpb.edu.br` não
é um comando.

| Entrada        | Efeito                                                                |
|----------------|-----------------------------------------------------------------------|
| `<url>`        | Visita uma url disponível. Erro: `PageNotFound (404)`.                |
| `/<página>`    | Visita uma página interna da url atual. Erro: `PageNotFound (404)`.   |
| `#add <url>`   | Adiciona uma url às disponíveis. Erro: `UrlCannotBeAdded`.            |
| `#back`        | Volta à última url visitada. Erro: `EmptyNavigationHistory`.          |
| `#showhist`    | Exibe o histórico de navegação.                                       |
| `#help`        | Lista todos os comandos.                                              |
| `#quit`        | Encerra o navegador.                                                  |

Banco de urls
-------------

Cada url pai tem um arquivo toml em disco nomeado com a própria url, lido na
inicialização e persistido ali pelo `#add`. O array começa pela url pai e segue
com suas páginas internas, como no arquivo `www.ifpb.edu.br`:

```toml
browser_history_urls = [
    "www.ifpb.edu.br",
    "www.ifpb.edu.br/tsi",
    "www.ifpb.edu.br/tsi/professores",
]
```

O `make clean` remove todos os arquivos `www.*` da raiz do projeto.

Implementação
-------------

Detalhes de implementação em [docs/IMPLEMENTATION_DETAILS.md](docs/IMPLEMENTATION_DETAILS.md).

Formatação
----------

Dependências:

-	[uv](https://docs.astral.sh/uv/) no `PATH`

```
make fmt
```
