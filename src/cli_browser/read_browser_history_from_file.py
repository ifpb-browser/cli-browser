from glob import glob

import tomli

from cli_browser.main import BROWSER_HISTORY_URLS_KEY

URL_FILES_GLOB = "www.*"


def read_browser_history_from_file() -> list[str]:
    browser_history_urls: list[str] = []

    for url_file_path in sorted(glob(URL_FILES_GLOB)):
        browser_history_urls.extend(read_url_file(url_file_path))

    return browser_history_urls


def read_url_file(url_file_path: str) -> list[str]:
    try:
        with open(url_file_path, "rb") as url_file:
            data = tomli.load(url_file)
    except FileNotFoundError:
        return []

    return data.get(BROWSER_HISTORY_URLS_KEY, [])
