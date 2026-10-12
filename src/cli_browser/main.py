import sys

from cli_browser.browser import Browser


def main() -> int:
    print("cli-browser", file=sys.stdout)
    browser = Browser()
    browser.handle()
    return 0


if __name__ == "__main__":
    main()
