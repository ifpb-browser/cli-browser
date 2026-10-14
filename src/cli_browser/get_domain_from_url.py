from cli_browser.main import URL_PATTERN


def get_domain_from_url(url: str) -> str:
    match = URL_PATTERN.match(url)

    if match is None:
        return ""

    return match.group("domain_name")
