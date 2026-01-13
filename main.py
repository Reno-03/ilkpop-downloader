#! python3
# kpopDownloader.py - downloads kpop songs based on the search link on ilkpop.com

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4

# get a request for the main website to get download link for each song
page_num = 1
search_key = 'Stray Kids'
type_radio = 'artist'

# different url request for page 1 and other pages
if page_num == 1:
    res = requests.get(f'https://www.ilkpop.com/site_59.xhtml?get-q={search_key}&get-type={type_radio}')

else:
    res = requests.get(f'https://www.ilkpop.com/site_59.xhtml?get-q={search_key}&get-n={page_num}&get-type={type_radio}')
    
res.raise_for_status()

# create a soup using bs4 and find the elements the contain the download link
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('td a')

# set-up first the driver, with the adblocker extension
browser = webdriver.Chrome()
browser.get('https://google.com')
time.sleep(2)

# iterate each download link
for link in links:
    url = f"https://ilkpop.com/{link.get('href')}"
    browser.get(url)

    download_elem = browser.find_element(By.CSS_SELECTOR, '#gotolink')

    main_window = browser.current_window_handle
    download_elem.click()

    time.sleep(2)

    # used to delete the pop-up windows that appears after clicking the download link
    for window in browser.window_handles:
        if window != main_window:
            browser.switch_to.window(window)
            browser.close()

    # go back to the main window
    browser.switch_to.window(main_window)

browser.quit()