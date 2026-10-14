from cli_browser.add_url_to_hierarchy import add_url_to_hierarchy
from cli_browser.clear_terminal import clear_terminal
from cli_browser.find_url_in_hierarchy import find_url_in_hierarchy
from cli_browser.get_valid_history_list import get_valid_history_list
from cli_browser.url import Url
from cli_browser.url_can_be_added import url_can_be_added
from cli_browser.write_url_to_file import write_url_to_file


class Browser:
    def __init__(self) -> None:
        self.current_url: Url = Url("", [])
        self.available_urls: list[Url] = get_valid_history_list()
        self.history: list[Url] = []
        self.status_message: str = "Type #help to see every available command."

    def handle(self) -> None:
        while True:
            try:
                clear_terminal()
                print(self)
                user_input = input("url: ").strip()

                if user_input == "#quit":
                    print("Leaving browser.")
                    break

                self.handle_user_input(user_input)

            except (EOFError, KeyboardInterrupt):
                print("\nQuitting by brute force! (^C or ^D detected)...")
                break

    def handle_user_input(self, user_input: str) -> None:
        if user_input == "#help":
            self.status_message = self.get_commands_help_text()

        elif user_input == "#back":
            self.go_back_to_last_visited_url()

        elif user_input == "#showhist":
            self.status_message = f"Navigation history: {self.history}"

        elif user_input.startswith("#add "):
            self.add_url(user_input.removeprefix("#add "))

        elif user_input.startswith("#"):
            self.status_message = f"[ERROR]: UnknownCommand: {user_input}"

        elif user_input.startswith("/"):
            self.visit_url(f"{self.current_url.path}{user_input}")

        else:
            self.visit_url(user_input)

    def go_back_to_last_visited_url(self) -> None:
        if not self.history:
            self.status_message = "[ERROR]: EmptyNavigationHistory"

            return

        self.current_url = self.history.pop()
        self.status_message = f"Returned to {self.current_url}"

    def visit_url(self, url_path: str) -> None:
        found_url = find_url_in_hierarchy(self.available_urls, url_path)

        if found_url is None:
            self.status_message = f"[ERROR]: PageNotFound (404): {url_path}"

            return

        if found_url is self.current_url:
            return

        if self.current_url.path:
            self.history.append(self.current_url)

        self.current_url = found_url
        self.status_message = "Page found!"

    def add_url(self, url: str) -> None:
        if not url_can_be_added(url, self.available_urls):
            self.status_message = f"[ERROR]: UrlCannotBeAdded: {url}"

            return

        try:
            write_url_to_file(url)
        except OSError as exception:
            self.status_message = f"[ERROR]: {exception}"

            return

        add_url_to_hierarchy(self.available_urls, url)
        self.status_message = f"Added {url}"

    def get_commands_help_text(self) -> str:
        return """Available commands:
        <url>        visit an available url
        /<page>      visit an internal page of the current url
        #add <url>   add an url to the available ones
        #back        return to the last visited url
        #showhist    show the navigation history
        #help        show this help
        #quit        leave the browser"""

    def __str__(self) -> str:
        browser_interface_content = f"""
        =========================================
        [ CLI BROWSER ]
        =========================================
        Home    : {self.current_url}
        History : {self.history}
        -----------------------------------------
        Links available: {self.current_url.child_urls or []}
        -----------------------------------------
        {self.status_message}
        =========================================
        """

        return browser_interface_content
