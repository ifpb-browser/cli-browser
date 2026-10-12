import re

def url_is_valid(url: str)-> bool:
    match = re.match(r"^www\.[a-zA-Z0-9-]+\.[a-z]{2,}(?:\.[a-z]{2,})*(?:\/[^\s]*)?$", url)
    if match:
        return True
    else:
        return False

def validate_urls(urls: list[str]) -> list[str]:
    return list(filter(url_is_valid, urls))