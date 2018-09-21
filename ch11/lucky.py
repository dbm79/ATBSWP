#! python
# lucky.py
# This program will take a command-line search string, open a browser, and search for the string on google.com

import sys
import requests
import bs4
import webbrowser


def get_req(search_string):
    ''' Returns request object from online resource.

        Keyword arguments:
        search_string -- the string that will be usedfor the search and request

        Returns:
        req -- a request object
    '''

    print(f'Googling...{search_string}')   # Displayed wile getting request
    result = requests.get(f"https://www.google.com/search?q={search_string}")

    if not result.raise_for_status():
        return result


def get_links(req):

    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    links = soup.select('.r a')

    return links


def main(args):

    request = get_req(' '.join(args[1:]))

    links = get_links(request)

    # Open browser for each link
    to_open = min(5, len(links))

    for i in range(to_open):
        webbrowser.open(f"https://www.google.com/{links[i].get('href')}")


if __name__ == '__main__':
    main(sys.argv)
