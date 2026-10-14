from cli_browser.url import Url


def find_url_in_hierarchy(url_hierarchy: list[Url], url_path: str) -> Url | None:
    for url in url_hierarchy:
        if url.path == url_path:
            return url

        if url.child_urls is None:
            continue

        found_child_url = find_url_in_hierarchy(url.child_urls, url_path)

        if found_child_url is not None:
            return found_child_url

    return None
