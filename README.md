# Bulk Kpop Downloader

**Description:**  
This Python script downloads all Kpop songs **based on ARTIST** from [ilkpop.com](https://www.ilkpop.com) . It fetches search results using `requests` and handles the download process with `Selenium`, automatically closing any pop-up windows that appear.

---

## Features

- Search by artist.
- Download all songs in a specific automatically.
- Automatically closes pop-up tabs.
- Command-line interface for flexibility.

---

## Requirements

- Python 3.8+
- Google Chrome
- Python packages:
  - `requests`
  - `selenium`
  - `beautifulsoup4`
  - `webdriver-manager` (optional, recommended)

---

## Run the Script Locally

Open Command Prompt, clone the repository and go to directory:

```bash
git clone https://github.com/Reno-03/ilkpop-downloader.git
cd ilkpop-downloader
```

Install all Python packages using:

```bash
pip install -r requirements.txt
```

Run the script with:

```bash
python main.py --page=<PAGE_NUMBER> --search="<SEARCH_KEYWORD>"
```

### Examples

- Download page 1 results for Stray Kids:

```bash
python main.py --page=1 --search="Stray Kids"
```

- Download page 2 results for BTS:

```bash
python main.py --page=2 --search="BTS"
```

### Command-line arguments

| Argument     | Description                      | Default      |
|--------------|----------------------------------|--------------|
| `--page`     | Page number of search results    | 1            |
| `--search`   | Search keyword (artist/song)     | "Stray Kids" |

---

## How it works

1. Sends a GET request to `ilkpop.com` to fetch search results.
2. Parses HTML with `BeautifulSoup` to extract download links.
3. Opens each link with Selenium, clicks the download button.
4. Detects and closes any popup tabs.
5. Repeats for all links on the search results page.

---

## Notes

- Make sure Chrome version and ChromeDriver version match.  
- Pop-ups are automatically closed to avoid interruptions.  
- The script currently runs in a visible browser window (not headless).

## TODO

- Download all songs of an artist based on **ALL pages**.
- Download with **multiple artist** search queires.
- **Filter the number of songs downloaded** in a specific page.