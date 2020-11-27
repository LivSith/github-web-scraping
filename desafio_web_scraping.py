from bs4 import BeautifulSoup

import requests
        

def sraping(repo):
        
    html = requests.get("https://github.com/", repo).content

    soup = BeautifulSoup(html, 'html.parser')

    # traz todo o html print(soup.prettify())

    temperatura = soup.find("span", class_="author flex-self-stretch")
    result = temperatura
        
    return result


def read_txt():
    repositorios = open("repositories.txt", "r")
    for repo in repositorios:
        url = repo
    return url


#print (scraping(repo))
#print(sraping(read_txt()))


def play():
    repositorios = open("repositories.txt", "r")
    for repo in repositorios:
        print ('Web scraping do repositório: ', repo)
        print(sraping(read_txt())) #apenas chamar a função scraping
        print('Gravando dados na pasta resultados, do repositório: ', repo)
    
    return (print('Fim!'))

print (play())