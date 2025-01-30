Simple-Web-Scraper
Just as the names says, This is a simple web scraper. Currently It scrapes a single website using the "requests" and "BeautifulSoup4" imports. BeautifulSoup4 allows easy examination of HTML and lets us break it down into small chunks to clearly see lots of data from a website.

current capabilities
- Display raw HTML (in a prettified state using the .prettify() function of BeautifulSoup4)
- Display individual titles, Paragraphs, Links, images,
- decent command line interface

Future Plans
- pagination handling
- better designed command line interface
- respect for robots.txt files in websites
- delay when scrapping to avoid overwhelming a website with requests

Developed in Visual Studio Code

requires python
use pip to install requests and BeautifulSoup4
pip install requests
pip install BeautifulSoup4

running the program
python ./scraper-python.py https://www.example.com

The program will guide you through looking at the data.
