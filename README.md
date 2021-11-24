# rsscrape

Python script to extract news from RSS feeds and save it as json.

## Usage

```shell
$ python3 rsscrape.py
[INFO] Found 51 in 'feeds.txt'
[INFO] Requests 51 XMLs content
[INFO] Scrape 10 items
[INFO] Write 1250 json files to './items'
[INFO] 1648 json files in './items'
```

**Generates a directory `items` with the results:**

```txt
./items
    0a1c2b2da6e40ab4e54b8247bbbc1422.json
    fc8ddcf4cc0725bfa35564fb19e4a407.json
    fe15bf1383c382101984ea4fdc6a33ae.json
    ...
```

**Each json file correspondends to a single RSS item:**

```json
// f8b40f2bb091e41c53eb35528c433d7f.json 
{
    "title": "USA: Corona, war da was?",
    "link": "https://de.nachrichten.yahoo.com/usa-corona-war-135203870.html",
    "pubDate": "2021-11-23T13:52:03Z",
    "source": "ZEIT ONLINE",
    "guid": "usa-corona-war-135203870.html",
    "raw": "<item xmlns:media=\"http://search.yahoo.com/mrss/\"><title>USA: Corona, war da was?</title><link>https://de.nachrichten.yahoo.com/usa-corona-war-135203870.html</link><pubDate>2021-11-23T13:52:03Z</pubDate><source url=\"http://www.zeit.de/index\">ZEIT ONLINE</source><guid isPermaLink=\"false\">usa-corona-war-135203870.html</guid><media:content height=\"86\" url=\"https://s.yimg.com/uu/api/res/1.2/_rdWs7VS_33DY3PJWhkh6Q--~B/aD04MTA7dz0xNDQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/de/zeit_921/2c35cfd59ae80f62a1ecb89623d2a47f\" width=\"130\"/><media:credit role=\"publishing company\"/></item>"
}
```
