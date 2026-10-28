import tomli_w

from cli_browser.get_domain_from_url import get_domain_from_url
from cli_browser.main import BROWSER_HISTORY_URLS_KEY
from cli_browser.read_browser_history_from_file import read_url_file


def write_url_to_file(url: str) -> None:
    url_file_path = get_domain_from_url(url)
    browser_history_urls = read_url_file(url_file_path) or [url_file_path]

    if url != url_file_path:
        browser_history_urls.append(url)

    with open(url_file_path, "wb") as url_file:
        tomli_w.dump({BROWSER_HISTORY_URLS_KEY: browser_history_urls}, url_file)
