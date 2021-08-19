# Google News Scraper 2021 [Multilingual Supported]

[<img src="https://img.shields.io/static/v1?label=&message=Python&color=blue" />](https://github.com/topics/python) [<img src="https://img.shields.io/static/v1?label=&message=Web Scraping&color=orange" />](https://github.com/topics/web-scraping) [<img src="https://img.shields.io/static/v1?label=&message=Google&color=green" />](https://github.com/topics/google)

## Description

Google News Scraper: get latest news from [news.google.com](https://news.google.com) of any region and language to `csv` or `json` formats instantly.

## Requirements

- Python 3
- pip

## Installation

_Installing project files_:

```bash
git clone https://github.com/scrapewalrus/google-news-scraper-2021
```
_Installing project requirements_:

![](project_screenshots/requirements.png)

## Usage





## List of commands

Command | Expected Input
------------ | -------------
 `-k`| keyword of your choice
 `-l` | `ISO 639-1` code representation of your preferred language
 `-o` | `csv` or `json`
 `--keyword` | long form of `-k`
 `--location` | long form of `-l`
 `--output` | long form of `-o`
 











### Example of json 
```json
[
    {
        "title": "A Hello Kitty x Nike Air Presto Retro Is in the Works - Complex",
        "link": "https://www.complex.com/sneakers/hello-kitty-nike-air-presto-retro-release-date",
        "publication_date": "2021-08-18"
    },
    {
        "title": "Take an Official Look at the NBA x Nike SB Nyjah Free 2 \"Lakers\" - HYPEBEAST",
        "link": "https://hypebeast.com/2021/8/nba-nike-sb-nyjah-free-2-lakers-official-look-release-info-da3439-100",
        "publication_date": "2021-08-19"
    },
    {
        "title": "Nike Dunk Low Bordeaux DD1503-108 Release Date | HYPEBEAST - HYPEBEAST",
        "link": "https://hypebeast.com/2021/8/nike-dunk-low-bordeaux-dd1503-108-release-date",
        "publication_date": "2021-08-18"
    }
```


### Example of csv


## Frequently Asked Questions

### How many results can I expect to get?
You can expect up to 100 results since that's also the maximum you can get on https://news.google.com.
Results largely depend on supplied keyword and location.

### Does this scraper support bulk queries?
Unfortunately, this scraper doesn't support bulk queries. If you want more scalable approach for scraping latest news from Google, I suggest you checking 




