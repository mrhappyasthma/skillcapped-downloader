# Skillcapped Downloader

 A simple utility to download videos from skill capped.

 ## Installation

 The script requires [python3](https://www.python.org/downloads/).

 It also requires the following modules, which can be installed with `pip` (i.e. `python3 -m pip install <name>`):

 - [selenium](https://pypi.org/project/selenium/)
 - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Running the script

1. Grab any top-level skill capped course URL (e.g. `https://www.skill-capped.com/lol/browse/course/34w9xhmhdp/zbphpwz5xt` for `Mastering in Minutes: Wave Control` for LoL).

2. Run the script (`python3 skillcapped.py`).

3. When prompted, paste the URL in to the tool.

4. Wait for the files to download!

## TODOs / Feature Requests

- Read URLs/class names from a csv file
- Or (better yet) scrape them from the main page of a given skill capped game

- Add ability to download in different qualities (4k [default], 1080p, 720p)
