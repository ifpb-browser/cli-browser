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

Toda entrada é digitada no prompt `Write your input`. Comandos começam com `#`,
e o `#add` exige um espaço antes da url.

| Entrada      | Efeito                                                                       |
|--------------|------------------------------------------------------------------------------|
| `#add <url>` | Registra a url no histórico e a torna a url atual. Erro: `InvalidURLFormat`. |
| `#quit`      | Encerra o navegador.                                                         |

Qualquer outra entrada responde `Unknown input`, e `Ctrl+C` também encerra o
navegador.

Banco de urls
-------------

O histórico é lido de `browser_history.toml` na inicialização e persistido nesse
mesmo arquivo pelo `#add`:

```toml
browser_history_urls = [
    "www.ifpb.edu.br",
    "www.detran.pb.gov.br",
]
```

Formatação
----------

Dependências:

-	[uv](https://docs.astral.sh/uv/) no `PATH`

```
make fmt
```
