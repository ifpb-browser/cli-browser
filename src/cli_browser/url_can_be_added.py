from cli_browser.find_url_in_hierarchy import find_url_in_hierarchy
from cli_browser.get_domain_from_url import get_domain_from_url
from cli_browser.get_valid_history_list import url_is_valid
from cli_browser.url import Url


def url_can_be_added(url: str, available_urls: list[Url]) -> bool:
    if not url_is_valid(url):
        return False

    if find_url_in_hierarchy(available_urls, url) is not None:
        return False

    return not domain_root_is_taken(url, available_urls)


def domain_root_is_taken(url: str, available_urls: list[Url]) -> bool:
    domain_name = get_domain_from_url(url)
    domain_root = ".".join(domain_name.split(".")[:2])

    for available_url in available_urls:
        if available_url.path.startswith(f"{domain_root}."):
            return available_url.path != domain_name

    return False
