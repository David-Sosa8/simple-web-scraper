import sys
import requests
from bs4 import BeautifulSoup

def show(soup):
    print(soup.prettify())

def scrape(site):
    # make a get request and parse html and check that the website is reachable
    try:
        response = requests.get(site)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print ("Http Error:",err)
        sys.exit()

def extract(soup):
    extract_choice = False
    while(not extract_choice):
        print('Extract: ')
        print('1. Title')
        print('2. Paragraphs')
        print('3. Links')
        print('4. Images')
        print('5. Quit')
        extract_option = input()
        if extract_option == '1':
            print(soup.title.text)
        elif extract_option == '2':
            for paragraph in soup.find_all('p'):
                print(paragraph.text)
        elif extract_option == '3':
            for link in soup.find_all('a'):
                print(link.get('href'))
        elif extract_option == '4':
            for img in soup.find_all('img'):
                print(img.get('src'))
        elif extract_option == '5':
            extract_choice = True
        else:
            print('Invalid choice. Please choose a number between 1 and 5')    

if __name__ == '__main__': # starts the "main function"
    # check if the user has entered a website to scrape
    if len(sys.argv) < 2:
        print('Invalid number of arguments. Program requires 1 (the website to be scraped)')
        sys.exit()
    site = sys.argv[1] 
    
    # validate the site
    if not site.startswith('http'):
        print('Invalid website. Please enter a valid website (https://www.example.com)')
        sys.exit()

    # scrape the site
    soup = scrape(site)
    print('Your site has been scraped and is ready to be examined')    
    stop = False # used to end the loop and exit the program
    
    while(not stop):
        choice = input('Scrape: ')
        if choice == 'E':
            # start extracting specific data from the web scrape
            extract(soup)
        elif choice == 'HTML':
            # display the prettified HTML
            show(soup)
        elif choice == 'Q' or choice == 'quit' or choice == 'q':
            stop = True
        elif choice == 'H' or choice == 'help':
            print('H or help -> displays this help page')
            print('E -> start extracting specific data from the web scrape')
            print('HTML -> display prettified HTML from your website')
        else:
            print('Invalid choice. Please choose a valid option or type H for help')