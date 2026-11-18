from os import makedirs

from cli_browser.main import PAGE_CONTENT_FILE_NAME


def write_url_page_content(url: str, page_content: str) -> None:
    makedirs(url, exist_ok=True)

    with open(f"{url}/{PAGE_CONTENT_FILE_NAME}", "w") as page_content_file:
        page_content_file.write(page_content)
