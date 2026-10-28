Detalhes de implementação
=========================

-	**Classes Browser e Url como sistema de urls**: o `Browser` guarda o estado da
	navegação e cada url é uma instância de `Url` que aninha suas páginas internas
	em `child_urls`, em no máximo dois níveis, com os netos recebendo `None`.

```python
    def __init__(self, path: str, child_urls: "list[Url] | None") -> None:
        self.path: str = path
        self.child_urls: list[Url] | None = child_urls
```

[src/cli_browser/url.py#L2-L4](https://github.com/ifpb-browser/cli-browser/blob/d48a00a0caaec535d11fb9f57b0ff7f90b6df0a2/src/cli_browser/url.py#L2-L4)

-	**Modularização das funções**: cada arquivo expõe uma única função com o nome
	do próprio arquivo, e as composições acontecem por delegação.

```python
def compile_urls_hierarchy(urls: list[str]) -> list[Url]:
    url_hierarchy: list[Url] = []

    for url in urls:
        add_url_to_hierarchy(url_hierarchy, url)
```

[src/cli_browser/compile_urls_hierarchy.py#L5-L9](https://github.com/ifpb-browser/cli-browser/blob/d48a00a0caaec535d11fb9f57b0ff7f90b6df0a2/src/cli_browser/compile_urls_hierarchy.py#L5-L11)

-	**Validação do formato das urls com regex**: uma única expressão compilada
	descreve o formato aceito e separa o domínio dos endpoints em grupos nomeados,
	sendo `url_is_valid` a única função que executa o match.

```python
URL_PATTERN = re.compile(
    r"^(?P<domain_name>www\.[a-zA-Z0-9-]+(?:\.[a-z]{2,})+)"
    r"(?P<page_endpoints>(?:/[a-zA-Z0-9._-]+)*)/?$"
)
```

[src/cli_browser/main.py#L5-L8](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/main.py#L5-L8)

-	**Armazenamento e parsing das urls**: cada url pai tem um arquivo toml em disco
	nomeado com a própria url, cujo array começa por ela e segue com suas páginas
	internas, lido com `tomli` na inicialização e escrito com `tomli_w` pelo `#add`.

```py
    url_file_path = get_domain_from_url(url)
    browser_history_urls = read_url_file(url_file_path) or [url_file_path]
```

[src/cli_browser/write_url_to_file.py#L9-L10](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/write_url_to_file.py#L9-L10)

-	**Exceções do projeto**: toda exceção é tratada e virada mensagem na interface,
	sendo `OSError` na escrita do arquivo, `EOFError` e `KeyboardInterrupt` no loop
	de entrada e `OSError` com `ValueError` na construção do `Browser`.

```python
        try:
            write_url_to_file(url)
        except OSError as exception:
            self.status_message = f"[ERROR]: {exception}"
```

[src/cli_browser/browser.py#L88-L91](https://github.com/ifpb-browser/cli-browser/blob/d48a00a0caaec535d11fb9f57b0ff7f90b6df0a2/src/cli_browser/browser.py#L88-L91)

-	**Interface**: a tela é redesenhada do zero a cada interação pelo
	`clear_terminal()`, que envia o código ANSI `\033c` antes de cada print, e o
	`__str__` do `Browser` monta o conteúdo com heredoc.

```python
        Home    : {self.current_url}
        History : {self.history}
        -----------------------------------------
        Links available: {self.current_url.child_urls or []}
```

[src/cli_browser/browser.py#L113-L116](https://github.com/ifpb-browser/cli-browser/blob/d48a00a0caaec535d11fb9f57b0ff7f90b6df0a2/src/cli_browser/browser.py#L113-L116)

-	**Padrões mantidos**: formatação pelo `ruff format`, uma responsabilidade por
	função, nenhum `if` aninhado, com decisões encadeadas e saídas antecipadas, e
	`main.py` reduzido às constantes compartilhadas e à chamada do `Browser`.

```python
def main() -> int:
    from cli_browser.browser import Browser

    try:
        browser = Browser()
    except (OSError, ValueError) as exception:
        print(f"[ERROR]: {exception}", file=sys.stderr)

        return 1

    browser.handle()

    return 0
```

[src/cli_browser/main.py#L11-L23](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/main.py#L11-L23)
