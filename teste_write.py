import os

dir = './resultado'
os.mkdir(dir)

arquivo = open('resultado/teste-novo-arquivo.txt', 'w')
arquivo.write('nova linha')
arquivo.close()