from cli_browser.read_browser_history_from_file import read_browser_history_from_file


class Browser:
    def __init__(self):
        self.current_url: str = ""
        self.history: list[str] = read_browser_history_from_file(
            "./browser_history_toml"
        )
