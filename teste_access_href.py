from bs4 import BeautifulSoup
import re
import requests

pages = set()

def get_links(page_url):
    pattern = re.compile("^(/)")
    html = requests.get(page_url).text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a", href=pattern):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)
                get_links(new_page)
        
get_links("https://www.climatempo.com.br/")