class Url:
    def __init__(
        self, path: str, child_urls: "list[Url] | None", page_content: str
    ) -> None:
        self.path: str = path
        self.child_urls: list[Url] | None = child_urls
        self.page_content: str = page_content

    def __repr__(self) -> str:
        return self.path
