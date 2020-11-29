import os
from bs4 import BeautifulSoup
import requests
import lxml

import pandas as pd


search_url = 'https://github.com/frontpressorg/frontpress'
base_url = 'https://github.com/'
repo_url = 'frontpressorg/frontpress'


def export_table_and_print(data):
    #cria tabela de resultado    
    table = pd.DataFrame(data, columns=['Files', 'URLs'])
    table.index = table.index + 1
    # cria pasta resultado
    dir = './resultados'
    os.mkdir(dir)
    # escreve resultado
    repo_name = (repo_url.lower().replace('/', '_'))
    file_name = "resultados/"+repo_name+"_scraping.txt"
    table.to_csv(file_name, sep=',', encoding='utf-8', index=False)
    print('Scraping done. Here are the results:')
    print(table)


    
def get_repo_data(file):
    name_file = file.find('a', class_='js-navigation-open link-gray-dark').text
    url_file = file.find('a')['href'] if name_file else ''
        
    data['Files'].append(name_file if name_file else '')
    data['URLs'].append(url_file if url_file else '')
    
# HTTP GET requests
page = requests.get(search_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')
    list_all_files = bs.findAll("div", class_="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item")
    
    data = {
        'Files': [],
        'URLs': [],
    }
        
    for file in list_all_files:
        get_repo_data(file)
    
    export_table_and_print(data)
  
parse_page(url)
#print(data)