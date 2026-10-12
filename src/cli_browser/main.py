import sys
from cli_browser.browser import browser

def main() -> int:
    print("cli-browser", file=sys.stdout)
    browser = browser()
    browser.handle()
    return 0

if __name__ == "__main__":
    main()

