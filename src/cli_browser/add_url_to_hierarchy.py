from cli_browser.find_url_in_hierarchy import find_url_in_hierarchy
from cli_browser.get_domain_from_url import get_domain_from_url
from cli_browser.get_page_endpoints_from_url import get_page_endpoints_from_url
from cli_browser.url import Url

MAXIMUM_INTERNAL_PAGE_DEPTH = 2
MAXIMUM_INTERNAL_LINKS_PER_PAGE = 2


def add_url_to_hierarchy(url_hierarchy: list[Url], url: str) -> None:
    domain_name = get_domain_from_url(url)
    parent_url = find_url_in_hierarchy(url_hierarchy, domain_name)

    if parent_url is None:
        parent_url = Url(domain_name, [])
        url_hierarchy.append(parent_url)

    page_endpoints = get_page_endpoints_from_url(url)[:MAXIMUM_INTERNAL_PAGE_DEPTH]

    for page_depth, page_endpoint in enumerate(page_endpoints, start=1):
        child_urls = parent_url.child_urls

        if child_urls is None:
            break

        page_path = f"{parent_url.path}/{page_endpoint}"
        child_url = find_url_in_hierarchy(child_urls, page_path)

        if child_url is None:
            if len(child_urls) == MAXIMUM_INTERNAL_LINKS_PER_PAGE:
                break

            child_url = Url(
                page_path, [] if page_depth < MAXIMUM_INTERNAL_PAGE_DEPTH else None
            )
            child_urls.append(child_url)

        parent_url = child_url
