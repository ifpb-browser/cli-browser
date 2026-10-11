import tomllib


def read_browser_history_from_file(file: str) -> list[str]:
    with open(file, "rb") as f:
        data = tomllib.load(f)
    return data["browser_history_urls"]
