from cli_browser.main import PAGE_CONTENT_FILE_NAME


def read_url_page_content(url_path: str) -> str:
    try:
        with open(f"{url_path}/{PAGE_CONTENT_FILE_NAME}") as page_content_file:
            return page_content_file.read()
    except OSError:
        return ""
