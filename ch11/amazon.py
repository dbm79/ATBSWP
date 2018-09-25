# amazon.py
# This program will take the search phrases from the command line, seach for them on Amazon.com
# and open the top links in the browser

import requests
from bs4 import BeautifulSoup
import webbrowser
import sys


def main(arguments):

    url = 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=chess'

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    test = soup.find_all('s-item-container')
    print(test)


if __name__ == '__main__':
    main(' '.join(sys.argv[1:]))
