"""Check generated textbook HTML links, assets and anchors."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "_build" / "html"


class Page(HTMLParser):
    def __init__(self, path: Path):
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for key in ("id", "name"):
            if key in values:
                self.ids.add(values[key])
        for key in ("href", "src"):
            if key in values:
                self.links.append(values[key])


def main() -> None:
    pages = {path.resolve(): Page(path) for path in HTML.glob("**/*.html") if "_static" not in path.relative_to(HTML).parts}
    checked = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or link.startswith("javascript:"):
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.exists(), f"Missing target {link} from {path.relative_to(HTML)}"
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f"Missing anchor {link} from {path.relative_to(HTML)}"
            checked += 1
    print(f"Validated {len(pages)} HTML pages and {checked} local links/assets.")


if __name__ == "__main__":
    main()
