import sys

from cli_browser.browser import Browser


def main() -> int:
    print("cli-browser", file=sys.stdout)
    browser = Browser()
    browser.handle()
    print(browser.__str__())
    return 0


if __name__ == "__main__":
    main()
