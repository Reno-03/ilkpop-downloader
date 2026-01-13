#! python3
# kpopDownloader.py - downloads kpop songs based on the search link on ilkpop.com

import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
import argparse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
import os

# get a request for the main website to get download link for each song using parser
parser = argparse.ArgumentParser(description="Download Kpop songs from ilkpop.com based on artist name")
parser.add_argument("--page", type=int, default=1, help="Page number to search")
parser.add_argument("--search", type=str, default="Stray Kids", help="Search keyword")
args = parser.parse_args()

# variables used in this script
page_num = args.page
search_key = args.search
type_radio = 'artist'

# Function to sanitize filename/folder names
def sanitize_name(name):
    # Remove invalid characters for Windows filenames
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Remove leading/trailing spaces and dots
    name = name.strip('. ')
    return name

# create download directory if not exists
download_dir = 'kpop_songs'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Sanitize the artist folder name
safe_artist_name = sanitize_name(search_key)
download_artist_dir = os.path.join(download_dir, safe_artist_name)
if not os.path.exists(download_artist_dir):
    os.makedirs(download_artist_dir)

print(f"Download folder: {download_artist_dir}\n")

# different url request for page 1 and other pages
if page_num == 1:
    res = requests.get(f'https://www.ilkpop.com/site_59.xhtml?get-q={search_key}&get-type={type_radio}')

else:
    res = requests.get(f'https://www.ilkpop.com/site_59.xhtml?get-q={search_key}&get-n={page_num}&get-type={type_radio}')
    
res.raise_for_status()

# create a soup using bs4 and find the elements the contain the download link
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('td a')

# set-up first the driver using webdriver manager
chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" 

# Optional: run headless
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

browser.get('https://google.com')
time.sleep(10)  # wait for brave to load

# iterate each download link
for idx, link in enumerate(links, 1):
    try:
        url = f"https://ilkpop.com/{link.get('href')}"
        print(f"\n[{idx}/{len(links)}] Processing: {url}")
        
        browser.get(url)
        
        # Wait for page to load
        wait = WebDriverWait(browser, 10)
        
        # Extract the href directly without clicking
        try:
            # Find the <a> tag containing the MP3 link
            download_link_elem = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="cloudflarestorage.com"]'))
            )
            mp3_url = download_link_elem.get_attribute('href')
            print(f"Found MP3 URL: {mp3_url[:100]}...")
            
            # Download using requests instead of Selenium
            print("Downloading...")
            mp3_response = requests.get(mp3_url, stream=True)
            mp3_response.raise_for_status()
            
            # Extract filename from URL
            if 'filename%3D' in mp3_url:
                filename = mp3_url.split('filename%3D')[1].split('&')[0].replace('%2520', ' ')
            else:
                filename = f"song_{idx}.mp3"
            
            filename = sanitize_name(filename)

            filepath = os.path.join(download_artist_dir, filename)
            
            # Save the file
            with open(filepath, 'wb') as f:
                for chunk in mp3_response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✓ Downloaded: {filename}")
            
        except Exception as e:
            print(f"✗ Failed to download: {e}")
            continue
            
    except Exception as e:
        print(f"✗ Error processing {url}: {e}")
        continue

browser.quit()