from cli_browser.main import URL_PATTERN


def get_page_endpoints_from_url(url: str) -> list[str]:
    match = URL_PATTERN.match(url)

    if match is None:
        return []

    page_endpoints = match.group("page_endpoints").split("/")

    return [page_endpoint for page_endpoint in page_endpoints if page_endpoint]
