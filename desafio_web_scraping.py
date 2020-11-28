from bs4 import BeautifulSoup

import requests
        

def sraping(repo):
        
    html = requests.get("https://github.com/", repo).content

    soup = BeautifulSoup(html, 'html.parser')

    # traz todo o html print(soup.prettify())

    repo_name = soup.find("span", class_="author flex-self-stretch")
    total_lines = soup.find("span", class_="github-gloc")
    result = repo_name
    print(total_lines)
    return result


def read_txt():
    repositorios = open("repositories.txt", "r")
    for repo in repositorios:
        url = repo
    return url


#print (scraping(repo))
#print(sraping(read_txt()))


def main():
    repositorios = open("repositories.txt", "r")
    for repo in repositorios:
        print ('Web scraping do repositório: ', repo)
        print(sraping(read_txt())) #apenas chamar a função scraping
        print('Gravando dados na pasta resultados, do repositório: ', repo)
        #teste saida txt
        print("----------------")
        print("Caminho relativo do projeto: ", repo)
        print()
    
    return (print('Fim!'))


if __name__ == '__main__':
    main()