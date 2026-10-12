from cli_browser.read_browser_history_from_file import read_browser_history_from_file


class Browser:
    def __init__(self) -> None:
        self.current_url: str = ""
        self.history: list[str] = read_browser_history_from_file(
            "./browser_history.toml"
        )

    def handle(self) -> None:
        print("Browser is ready! Waiting for user inputs...")

    def __str__(self) -> str:
        # This formats the list history, i`ll be adding a line break between links, you can remove it if you want
        history_str = "".join(f"  - {url}" for url in self.history)

        # O f""" (f-string com aspas triplas) é o equivalente ao heredoc no Python
        browser_interface_content = f"""
        =========================================
        [ CLI BROWSER ]
        =========================================
        URL Atual : {self.current_url if self.current_url else "Nenhuma (Página Inicial)"}
        -----------------------------------------
        Histórico :
        {history_str}
        =========================================
        """
        return browser_interface_content
