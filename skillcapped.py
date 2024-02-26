import os
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# NOTE: These values were found by hand using `inspect element` on chrome. They are a bit
# fragile as its possible they could easily change. But I couldn't find a more robust way.
VIDEO_TITLES_DIV_CLASS_NAME = 'css-1mkvlph'
VIDEO_IDS_DIV_ID_PREFIX = 'BrVidRow-'


def get_video(video_id, video_title, folder_name):
    """Downloads each .ts file part for the given video ID and then concatenates them all in to a final video
    file with the provided `video_title`.
    """
    print("Downloading video ' " + video_title + "' with ID: " + video_id, flush=True)
    num = 1
    files = ''
    while num:
        piece_number = str(num).zfill(5)
        # 4500 = 4k, 2500 = 1080p, 1500 = 720p
        url = 'https://d13z5uuzt1wkbz.cloudfront.net/' + video_id + '/HIDDEN4500-' + piece_number + '.ts'
        req = requests.get(url)
        file_size = (len(req.content) / 1024) /1024
 
        if req.status_code == 200:
            file_name = url.split('/')[-1]
            download_sc(url)
            num = num + 1
            files += file_name + ' '
            print(f'Download file: {file_name} {file_size:.2f}Mb', flush=True)
        else:
            print(f'Downloaded {num-1} files.', flush=True)
            output_file_name = '"' + video_title + '.ts' + '"'
            output_file_name = output_file_name.replace(":", " - ")  # colons cannot be in windows file names
            print("output file name: " + output_file_name)
            os.system("cat " + files + " > " + output_file_name)
            os.system("rm " + files)
            print("Temporary files deleted...")
            os.system("mv " + output_file_name + ' "' + folder_name + '\\' + video_title + '.ts"')
            print(f"Video file {output_file_name} created.", flush=True)
            break


def download_sc(download_url):
    """Downloads an individual video file with the given URL."""
    file_name = download_url.split('/')[-1]
 
    with requests.get(download_url) as req:
        with open(file_name, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return file_name


def fetch_dynamic_url(dynamic_url):
    # Start by loading the web page dynamically with Selenium
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    browser = webdriver.Firefox()
    browser.get(url)

    # Wait until the dynamic data is available
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, VIDEO_TITLES_DIV_CLASS_NAME ))
        )
    except:
        browser.quit()

    soup = BeautifulSoup(browser.page_source, "html.parser")
    browser.quit()
    return soup


def extract_ids(soup):
    """Iterate all divs, should start with "BrVidRow-" prefix, with second part as ID"""
    video_ids = []
    for row in soup.find_all('div', id=re.compile(VIDEO_IDS_DIV_ID_PREFIX)):
        video_ids.append(row.get('id').split('-')[-1])
    return video_ids


def extract_titles(soup):
    """Find the titles from divs with class 'css-1mkvlph'."""
    video_titles = []
    num = 1
    for row in soup.find_all('div', attrs={'class': VIDEO_TITLES_DIV_CLASS_NAME }):
        video_titles.append(str(num) + ". " + row.get_text())
        num = num + 1
    return video_titles


in_file = open("inputs.txt", "r")
lines = in_file.readlines()

for line in lines:
    segments = line.split(",")
    # Any top-level URL from the class
    url = segments[1]
    folder_name = segments[0]

    os.system("mkdir " + '"' + folder_name + '"')

    soup = fetch_dynamic_url(url)
    video_ids = extract_ids(soup)
    video_titles = extract_titles(soup)

    print(video_ids)
    print(video_titles)

    for i in range(len(video_ids)):
        get_video(video_ids[i], video_titles[i], folder_name)

in_file.close()
