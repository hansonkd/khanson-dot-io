"""Check the static site's links and publication files using only the standard library."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent / "site"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        if tag == "img":
            assert "alt" in attrs, "Image missing alternative text"
            assert "width" in attrs and "height" in attrs, "Image missing dimensions"
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


page = (ROOT / "index.html").read_text()
parser = SiteParser()
parser.feed(page)
assert parser.headings == 1, "Expected one primary heading"
for link in parser.links:
    url = urlsplit(link)
    if url.scheme or url.netloc:
        continue
    if url.path:
        path = ROOT / unquote(url.path.lstrip("/"))
        assert path.is_file(), f"Missing linked file: {link}"
    elif url.fragment:
        assert url.fragment in parser.ids, f"Missing anchor: {link}"

for stylesheet in (ROOT / "assets").glob("*.css"):
    for link in re.findall(r"url\(['\"]?([^)'\"]+)", stylesheet.read_text()):
        assert (stylesheet.parent / link).is_file(), f"Missing CSS asset: {link}"
for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S):
    json.loads(data)
ET.parse(ROOT / "sitemap.xml")
assert (ROOT / "CNAME").read_text().strip() == "khanson.io"
assert (ROOT / ".nojekyll").is_file()
print(f"Site checks passed: {len(parser.links)} links, fonts, structured data, sitemap, and domain.")
