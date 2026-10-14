from cli_browser.add_url_to_hierarchy import add_url_to_hierarchy
from cli_browser.url import Url


def compile_urls_hierarchy(urls: list[str]) -> list[Url]:
    url_hierarchy: list[Url] = []

    for url in urls:
        add_url_to_hierarchy(url_hierarchy, url)

    return url_hierarchy
