import tomllib
import tomli_w

def write_url_to_file(file: str, url:str) -> None:
    try:
        with open(file, "rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        data = {"browser_history_urls": []}

    data["browser_history_urls"].append(url)

    with open(file, "wb") as f:
        tomli_w.dump(data,f)
        