# Skillcapped Downloader

 A simple utility to download videos from skill capped.

 ## Installation

 The script requires [python3](https://www.python.org/downloads/).

 It also requires the following modules, which can be installed with `pip` (i.e. `python3 -m pip install <name>`):

 - [selenium](https://pypi.org/project/selenium/)
 - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Running the script

1. Construct a comma-separate text file, with the format `<course_name>,<url>` where the URL is any top-level skill capped course URL (e.g. `Mastering in Minutes: Wave Control,https://www.skill-capped.com/lol/browse/course/34w9xhmhdp/zbphpwz5xt` for LoL). Each line should contain one of these pairs, separated by newlines.

2. Run the script (`python3 skillcapped.py`).

3. Wait for the files to download!

## TODOs / Feature Requests

- Scrape all skill capped videos from site

- Extract the class name from the HTML

- Add ability to download in different qualities (4k [default], 1080p, 720p)
