# Script to scrape a website to get the number of unique HTML elements
# Example: py web_scrape.py https://adrxone.github.io/Exercise-1

from bs4 import BeautifulSoup
import requests
import sys

# To keep track of the visited URLs
hrefs = ["/","index.html"]
elements = set()

def scrape(site, path):
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(site + path).text
    print(site + path)

    # Parse the html content using any parser
    s = BeautifulSoup(html_content, "html.parser")

    # Recurse to get all the anchors
    for i in s.find_all("a"):
        if ('href' in i.attrs):
            href = i.attrs['href']
            if not href.startswith(("https", "http", "www")):
                href = "/" + href if not href.startswith("/") else href
                if href not in hrefs:
                    hrefs.append(href)
                    scrape(site, href)

    # Add distinctive HTML elements
    elements.update([tag.name for tag in s.find_all()])


if __name__ == "__main__":
    site = sys.argv[1]
    scrape(site, "")

    print(sorted(elements))
    print(f'Number of Unique HTML Elements is {len(elements)}')