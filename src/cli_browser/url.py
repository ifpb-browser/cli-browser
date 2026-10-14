class Url:
    def __init__(self, path: str, child_urls: "list[Url] | None") -> None:
        self.path: str = path
        self.child_urls: list[Url] | None = child_urls

    def __repr__(self) -> str:
        return self.path
