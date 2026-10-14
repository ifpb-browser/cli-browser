import tomli

from cli_browser.main import BROWSER_HISTORY_FILE_PATH, BROWSER_HISTORY_URLS_KEY


def read_browser_history_from_file() -> list[str]:
    try:
        with open(BROWSER_HISTORY_FILE_PATH, "rb") as browser_history_file:
            data = tomli.load(browser_history_file)
    except FileNotFoundError:
        return []

    return data.get(BROWSER_HISTORY_URLS_KEY, [])
