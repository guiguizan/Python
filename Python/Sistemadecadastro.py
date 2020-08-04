#Crie um cadastro de usuário em Python, que armazene nome, idade e um numero de cadastro aleatorio de zero a mil.
#Com a possibilidade de adicionar, remover, listar e filtrar usuarios cadastrados.

lista = []

from random import seed
import random

seed(1)



# adicionar a lista
def add(x,y, z):
    for i in range(len(lista)):
        if x in lista:
            print('ja possui na lista')
            return
    aux = x + ',' + y + ',' + z
    lista.append(aux)
    print('numero adicionado')



#remover
def remove(x):
    if x in lista:
        lista.remove[x]




#filtrar
def filtrar(x):
    for i in range(len(lista)):
        if x in lista[i]:
            print(lista[i])


while True:
    funcao = int(input('digite 1 para adicionar, 2 pra remover, 3 pra listar, 4 pra filtrar:  '))

    # add
    if funcao == 1:
        n = input('digite o nome para cadastro: ')
        i = input('digite a idade: ')
        id = str(random.randint(0, 1000))
        add(n,i,id)
        print(lista)

    # remove
    if funcao == 2:
        n = input('digite para remover da lista: ')
        remove(n)

    # listar
    if funcao == 3:
        for i in range(len(lista)):
            print(lista[i])

    # filtrar
    if funcao == 4:
        n = input('digite para filtrar na lista: ')
        filtrar(n)