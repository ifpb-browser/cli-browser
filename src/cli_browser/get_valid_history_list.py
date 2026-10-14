from cli_browser.compile_urls_hierarchy import compile_urls_hierarchy
from cli_browser.main import URL_PATTERN
from cli_browser.read_browser_history_from_file import read_browser_history_from_file
from cli_browser.url import Url


def get_valid_history_list() -> list[Url]:
    browser_history_urls = read_browser_history_from_file()
    valid_urls = [url for url in browser_history_urls if url_is_valid(url)]

    return compile_urls_hierarchy(valid_urls)


def url_is_valid(url: str) -> bool:
    return URL_PATTERN.match(url) is not None
