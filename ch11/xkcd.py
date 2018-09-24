#! python
# xkcd.py
# This program will download all of the XKCD.com comic images until it reaches the 1st one

import requests
from bs4 import BeautifulSoup
import os


def main():

    url = 'https://www.xkcd.com/'
    # create directory we will store the comics
    os.makedirs('xkcd', exist_ok=True)

    while not url.endswith('#'):
        # Download the image
        print(f'Downloading page: {url}')
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text)

        # Find the URL of the comic image.
        comic_element = soup.select('#comic img')

        if comic_element == []:
            print('Could not find comic!')
        else:
            image_url = f"https:{comic_element[0].get('src')}"
            print(image_url)

            # Download the image.
            print(f'Downloading file: {image_url}')
            res = requests.get(image_url)
            res.raise_for_status()

        # Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(image_url)), 'wb') as image_file:

            for chunk in res.iter_content(100000):
                image_file.write(chunk)

        # Get the Prev button's url.
        prev_link = soup.select('a[rel="prev"]')[0]
        url = f'https://www.xkcd.com{prev_link.get("href")}'

    print(f'Done!!')


if __name__ == '__main__':
    main()
