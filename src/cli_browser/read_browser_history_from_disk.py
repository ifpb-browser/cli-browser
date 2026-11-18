from glob import glob
from os import listdir
from os.path import isdir

URL_FOLDERS_GLOB = "www.*"


def read_browser_history_from_disk() -> list[str]:
    browser_history_urls: list[str] = []

    for url_folder_path in sorted(glob(URL_FOLDERS_GLOB)):
        if not isdir(url_folder_path):
            continue

        browser_history_urls.extend(read_url_folder(url_folder_path))

    return browser_history_urls


def read_url_folder(url_path: str) -> list[str]:
    url_paths = [url_path]

    for child_folder_name in sorted(listdir(url_path)):
        child_url_path = f"{url_path}/{child_folder_name}"

        if not isdir(child_url_path):
            continue

        url_paths.extend(read_url_folder(child_url_path))

    return url_paths
