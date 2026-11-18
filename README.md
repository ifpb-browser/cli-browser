cli-browser
===========

Navegador web de linha de comando.

Execução
--------

```
make run
```

Limpar histŕico de URLs e dependências
--------

```
make clean
```

Comandos
--------

Toda entrada é digitada no prompt `url:`, com exceção do conteúdo da página, que
o `#add` pede em seguida no prompt `content:`. Comandos começam com `#`, e os que
recebem uma url exigem um espaço antes dela, portanto `#addwww.ifpb.edu.br` não
é um comando.

| Entrada        | Efeito                                                                |
|----------------|-----------------------------------------------------------------------|
| `<url>`        | Visita uma url disponível. Erro: `PageNotFound (404)`.                |
| `/<página>`    | Visita uma página interna da url atual. Erro: `PageNotFound (404)`.   |
| `#add <url>`   | Adiciona uma url e pede seu conteúdo. Erro: `UrlCannotBeAdded`.       |
| `#back`        | Volta à última url visitada. Erro: `EmptyNavigationHistory`.          |
| `#showhist`    | Exibe o histórico de navegação.                                       |
| `#help`        | Lista todos os comandos.                                              |
| `#quit`        | Encerra o navegador.                                                  |

Banco de urls
-------------

Cada url pai é uma pasta em disco nomeada com a própria url, lida na
inicialização e persistida ali pelo `#add`. Dentro dela fica o arquivo sem
extensão `url_page_content`, com o texto puro digitado no prompt `content:`, e
cada página interna é uma pasta que segue a mesma regra, como na pasta
`www.ifpb.edu.br`:

```
www.ifpb.edu.br/
├── url_page_content
└── tsi/
    ├── url_page_content
    └── professores/
        └── url_page_content
```

As páginas internas de uma url são indexadas pelos nomes das pastas dentro dela.

O `make clean` remove todas as pastas `www.*` da raiz do projeto.

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

## Video de demonstração

https://github.com/user-attachments/assets/5bc8711a-5ee1-4a48-be00-8a60ef636098
