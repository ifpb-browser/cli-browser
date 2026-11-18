import re
import sys

PAGE_CONTENT_FILE_NAME = "url_page_content"
URL_PATTERN = re.compile(
    r"^(?P<domain_name>www\.[a-zA-Z0-9-]+(?:\.[a-z]{2,})+)"
    r"(?P<page_endpoints>(?:/[a-zA-Z0-9._-]+)*)/?$"
)


def main() -> int:
    from cli_browser.browser import Browser

    try:
        browser = Browser()
    except (OSError, ValueError) as exception:
        print(f"[ERROR]: {exception}", file=sys.stderr)

        return 1

    browser.handle()

    return 0


if __name__ == "__main__":
    main()
