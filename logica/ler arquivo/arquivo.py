lista = ['Kerolain', 'Andressa']

with open ('nome.txt', 'a') as arquivo:
    for i in lista:
        arquivo.write (i + '\n')

with open ('nome.txt', 'r') as arquivo:
    for i in arquivo:
        print(i)