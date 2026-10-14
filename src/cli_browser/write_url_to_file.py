import tomli_w

from cli_browser.main import BROWSER_HISTORY_FILE_PATH, BROWSER_HISTORY_URLS_KEY
from cli_browser.read_browser_history_from_file import read_browser_history_from_file


def write_url_to_file(url: str) -> None:
    browser_history_urls = read_browser_history_from_file()
    browser_history_urls.append(url)

    with open(BROWSER_HISTORY_FILE_PATH, "wb") as browser_history_file:
        tomli_w.dump(
            {BROWSER_HISTORY_URLS_KEY: browser_history_urls}, browser_history_file
        )
