import aiohttp
import asyncio
import json

from lxml import etree
from pathlib import Path
from hashlib import md5
from glob import glob

# TODO: add cli functionality
# TODO: add single rss request per cli

FEEDS_SOURCE = "feeds.txt"
TARGET_PATH = "./items"

Path(TARGET_PATH).mkdir(exist_ok=True)

with open(FEEDS_SOURCE) as f:
    FEEDS = [feed.replace("\n", "") for feed in f.readlines()]

print(f"[INFO] Found {len(FEEDS)} in '{FEEDS_SOURCE}'")


async def req(url, session):
    r = await session.get(url)
    if r.status == 200:
        data = await r.text()
        return data
    else:
        return None


def extract_items(xml):
    items = []

    root = etree.fromstring(xml.encode())
    for item in root.xpath("//item"):
        headline = {}
        for child in item:
            if child.tag[0] != "{":
                if child.text:
                    headline[child.tag] = child.text

        if headline:
            headline["raw"] = etree.tostring(item).decode("utf-8")
            items.append(headline)

    return items


async def main():
    async with aiohttp.ClientSession() as session:
        xmls = await asyncio.gather(*(req(feed, session) for feed in FEEDS))

    all_items = []
    for xml, feed in zip(xmls, FEEDS):
        items = []
        if xml:
            try:
                items = extract_items(xml)
                all_items += items
            except etree.XMLSyntaxError:
                pass
        if not items:
            print(f"[WARNING] {len(items)} items found in source '{feed}'")

    print(f"[INFO] Requests {len(xmls)} XMLs content")
    print(f"[INFO] Scrape {len(items)} items")

    for item in all_items:
        filename_hashed = md5(json.dumps(item).encode()).hexdigest()
        filename_hashed = f"{filename_hashed}.json"
        with open(f"{TARGET_PATH}/{filename_hashed}", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    print(f"[INFO] Write {len(all_items)} json files to '{TARGET_PATH}'")

    all_files_amount = len(glob(f"{TARGET_PATH}/*.json"))
    print(f"[INFO] {all_files_amount} json files in '{TARGET_PATH}'")


if __name__ == "__main__":
    asyncio.run(main())
