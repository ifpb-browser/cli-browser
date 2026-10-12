from cli_browser.read_browser_history_from_file import read_browser_history_from_file
from cli_browser.validate_urls import url_is_valid
from cli_browser.write_url_to_file import write_url_to_file
from cli_browser.get_url_from_user_input import get_url_from_user_input

class Browser:
    def __init__(self) -> None:
        self.current_url: str = ""
        self.history: list[str] = read_browser_history_from_file(
            "./browser_history.toml"
        )

    def handle(self) -> None:
       while True:
            try:
                print(self)
                user_input = input("Write your input (#add <url> ou #quit): ")
                
                if user_input == "#quit":
                    print("Leavin' browser.")
                    break
                    
                elif user_input.startswith("#add "):
                    # using translation with regex to clean string
                    treated_url = get_url_from_user_input(user_input)
                    
                    try:
                        self.add_url_to_history(treated_url)
                        self.current_url = treated_url
                    except Exception as exception:
                        print(f"\n[ERROR]: {exception}")
                        
                else:
                    print("\n[ERROR]: Unknown input.")
                    
            except KeyboardInterrupt:
                print("\nQuitting by brute force! (^C detected)...")
                break
        
    def __str__(self) -> str:
        # This formats the list history, i`ll be adding a line break between links, you can remove it if you want
        history_str = "".join(f"  - {url}" for url in self.history)

        # O f""" (f-string com aspas triplas) é o equivalente ao heredoc no Python
        browser_interface_content = f"""
        =========================================
        [ CLI BROWSER ]
        =========================================
        Current URL : {self.current_url if self.current_url else "NONE (Index page)"}
        -----------------------------------------
        History :
        {history_str}
        =========================================
        """
        return browser_interface_content

    def add_url_to_history(self, url: str) ->  bool:
        if not url_is_valid(url):
            raise ValueError("InvalidURLFormat")
        self.history.append(url)
        write_url_to_file("./browser_history.toml", url)