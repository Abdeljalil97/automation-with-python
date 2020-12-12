import argparse
import logging
import sys
import re
import http.client
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG
#. Downloading and parsing the link
def process_link(source_link,text):
    logging.info(f'getting the url from {source_link}')
    parsed_url = urlparse(source_link)
    result = requests.get(source_link)
    if result.status_code != http.client.OK:
        logging.error(f'Error retrieving {source_link}:{result}')
        return []
    if 'html' not in result.headers['Content-type']:
        logging.info(f'Link {source_link} is not an HTML page')
        return []
    page = BeautifulSoup(result.text,'html.parser')
    search_text(source_link,page,text)
    return get_links(source_link,page)

def search_text(source_link,page,text):
#search the text in the link 
    for elemnet in page.find_all(text=re.compile(text,flags=re.IGNORECASE)):
        print(f'Link {source_link}: --> {element}')




#getting the URLS from the base_url
def get_links(parsed_url,page):
    links = []
    #retreive all of a tag from the page
    for element in page.find_all('a'):
        link = element.get('href')
        if not link:
            continue
        # avoid internal link
        if link.startswith('#'):
            continue
        # elimine email llink
        if link.startswith('mailto'):
             # Ignore other links like mailto
 # More cases like ftp or similar may be included here
            continue
        # Always accept local links
        if not link.startswith('http'):
            netloc = parsed_source.netloc
            scheme = parsed_source.scheme
            path = urljoin(parsed_source.path, link)
            link = f'{scheme}://{netloc}{path}'
        # Only parse links in the same domain
        if parsed_url.netloc not in link:
            continue
        links.append(link)
        return links



def main(base_url, to_search):
    checked_links = set()
    to_check = [base_url]
    max_checks = 10
    while to_check and max_checks:
        link = to_check.pop(0)
        links = process_link(link,text=to_search)
        checked_links.add(link)
        for link in links:
            if link not in checked_links:
                checked_links.add(link)
                to_check.append(link)
        max_checks -= 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-url',dest='url', type=str, help='the url')
    parser.add_argument('-p', type=str, help='the string to research')
    parser.add_argument('-o', dest='output', type=argparse.
            FileType('w'),
        help='output file', default=sys.stdout)

    args = parser.parse_args()

    main(args.url,args.p)
