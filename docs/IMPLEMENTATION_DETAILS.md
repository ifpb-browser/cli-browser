Detalhes de implementação
=========================

-	**Classes Browser e Url como sistema de urls**: o `Browser` guarda o estado da
	navegação e cada url é uma instância de `Url` que guarda o conteúdo da página
	em `page_content` e aninha suas páginas internas em `child_urls`, em no máximo
	dois níveis, com os netos recebendo `None`.

```python
        self.path: str = path
        self.child_urls: list[Url] | None = child_urls
        self.page_content: str = page_content
```

[src/cli_browser/url.py#L5-L7](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/url.py#L5-L7)

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

-	**Armazenamento das urls em pastas**: cada url é uma pasta nomeada com a
	própria url, então o caminho em disco é a própria url e o `makedirs` do `#add`
	cria a hierarquia inteira, com o conteúdo da página no arquivo sem extensão
	`url_page_content` e as páginas internas indexadas pelas pastas de dentro.

```python
def write_url_page_content(url: str, page_content: str) -> None:
    makedirs(url, exist_ok=True)

    with open(f"{url}/{PAGE_CONTENT_FILE_NAME}", "w") as page_content_file:
        page_content_file.write(page_content)
```

[src/cli_browser/write_url_page_content.py#L6-L10](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/write_url_page_content.py#L6-L10)

-	**Exceções do projeto**: toda exceção é tratada e virada mensagem na interface,
	sendo `OSError` na escrita do arquivo, `EOFError` e `KeyboardInterrupt` no loop
	de entrada e `OSError` com `ValueError` na construção do `Browser`.

```python
        try:
            write_url_page_content(url, page_content)
        except OSError as exception:
            self.status_message = f"[ERROR]: {exception}"
```

[src/cli_browser/browser.py#L91-L94](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/browser.py#L91-L94)

-	**Interface**: a tela é redesenhada do zero a cada interação pelo
	`clear_terminal()`, que envia o código ANSI `\033c` antes de cada print, e o
	`__str__` do `Browser` monta o conteúdo com heredoc.

```python
        Home    : {self.current_url}
        History : {self.history}
        -----------------------------------------
        Content : {self.current_url.page_content}
```

[src/cli_browser/browser.py#L116-L119](https://github.com/ifpb-browser/cli-browser/blob/main/src/cli_browser/browser.py#L116-L119)

-	**Padrões mantidos**: formatação pelo `ruff format`, uma responsabilidade por
	função, saídas antecipadas em vez de `if` aninhado, despacho de comandos com
	`match`, e `main.py` reduzido às constantes compartilhadas e à chamada do
	`Browser`.

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
