import os
import collections, functools, operator
from bs4 import BeautifulSoup

from decimal import Decimal
import requests
import lxml

import pandas as pd


search_url = 'https://github.com/frontpressorg/frontpress'
base_url = 'https://github.com/'
repo_url = 'frontpressorg/frontpress'


data = {
        'Extension': [],
        'Linhas': [],
        'Bytes': [],
    }


def export_table_and_print(data):
    #cria tabela de resultado    
    table = pd.DataFrame(data, columns=['Extension', 'Linhas', 'Bytes',])
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
    type_of_file = file.find('svg')['aria-label'] if name_file else ''
        
    #data['Files'].append(name_file if name_file else '')
    #data['Type_of_file'].append(type_of_file if type_of_file else '')
    
    new_repo_url = base_url+url_file
    new_page=requests.get(new_repo_url)
    
    extension_type = name_file.split('.')
    extension = extension_type[-1]
    
    
    
    if new_page.status_code == requests.codes.ok:
        bs_repo = BeautifulSoup(new_page.text, 'lxml')
        
        if type_of_file == 'File':
            find_dados = bs_repo.find("div", class_="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0").text
            
            dados_limpo = find_dados.lstrip()
            dados_list = dados_limpo.split()
            lines = Decimal(dados_list[0])
            size = Decimal(dados_list[-2])
            
            data['Extension'].append(extension)
            data['Linhas'].append(lines)
            data['Bytes'].append(size)
            
            
            #if extension not in data['Extension']:
                #data['Extension'].append(extension)
                #data['Linhas'].append(lines)
                #data['Bytes'].append(size)

        else:
            data['Linhas'].append('')
            data['Bytes'].append('')
            data['Extension'].append('')
            
        
#def parse_page(next_url):
    
# HTTP GET requests
page = requests.get(search_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')
        
    list_all_files = bs.findAll("div", class_="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item")
    
    
total_lines=0       
for file in list_all_files:
    get_repo_data(file)


export_table_and_print(data)

counter = collections.Counter() 

#parse_page(url)
#print(data)