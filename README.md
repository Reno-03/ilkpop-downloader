<h1 align="center">🎶 Bulk Kpop Downloader 🎶 </h1>

<p align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python"></a>
<a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-WebDriver-lightgreen" alt="Selenium"></a>
<a href="https://www.ilkpop.in/"><img src="https://img.shields.io/badge/ilKPOP-Web-darkgreen" alt="ilKPOP"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

<p align="center"> This Python script downloads all Kpop songs <b>based on ARTIST</b> from <a href="https://www.ilkpop.com" alt="ilKPOP">ilKPOP</a>. It fetches search results and handles the download process with <i>Requests</i> and <i>Selenium</i>.</p>

## Demo

<div align="center">
  <img src="/screenshots/demo.gif" height="400"/>
</div>

## Features

- Search by artist.
- Download all songs in a specific page automatically.
- Uses Chromium-based browser like Brave to remove pop-ups and ads.
- Command-line interface for flexibility.

## Requirements

- Python 3.8+
- Brave Browser (for no popups)
- Python packages:
  - `requests`
  - `selenium`
  - `beautifulsoup4`
  - `webdriver-manager` (optional, recommended)

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

### Song File Directory  

The downloaded songs are saved at:
```bash
/kpop_songs/<artist_name>/
```

## How it works

1. Sends a GET request to `ilkpop.com` to fetch search results.
2. Parses HTML with `BeautifulSoup` to extract download links.
3. Retrieves the MP3 URL then downloads it using Requests.
4. The downloaded file is renamed properly, including Korean characters.
5. Repeats for all links on the search results page.

## Notes

- Make sure Brave version and Brave version match.  
- Pop-ups are automatically closed to avoid interruptions.  
- The script currently runs in a visible browser window (not headless).

## TODO

- Download all songs of an artist based on **ALL pages**.
- Download with **multiple artist** search queires.
- **Filter the number of songs downloaded** in a specific page.
