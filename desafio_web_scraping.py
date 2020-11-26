from bs4 import BeautifulSoup

import requests


def sraping(x):
        
    html = requests.get(x).content

    soup = BeautifulSoup(html, 'html.parser')

    # traz todo o html print(soup.prettify())

    temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
        
    return temperatura.string


def read_txt():
    repositorios = open("repositories.txt", "r")
    for repo in repositorios:
        url = repo
    return url


#print (scraping(repo))
print(sraping(read_txt()))
    