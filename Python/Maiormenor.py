#Implemente um programa que insira numeros em uma lista, e possa descobrir o maior e o menor numero que nela contém.

lista = []



for j in range(4):
    n = (int(input('digite: ')))
    lista.append(n)

maior = lista[0]
menor = lista[0]


for i in range(1,len(lista)):
    if n < menor:
        menor = n
    if n > maior:
        maior = n



print(lista, maior, menor)
