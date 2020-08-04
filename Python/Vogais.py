#Implemente um código em Python que conte quantas letras tem de cada vogal tem dentro de uma lista de nomes fornecidos pelo usuario.

listaNomes = []


for i in range(3):
    nome = listaNomes.append(input('digite um nome: '))


print(listaNomes)

a = e = i = o = u = 0

for k in range (len(listaNomes)):
   for j in listaNomes[k]:
       if j == 'a':
           a += 1
       elif j == 'e':
           e += 1
       elif j == 'i':
           i += 1
       elif j == 'o':
           o += 1
       elif j == 'u':
           u += 1

print ('A = ' , a)
print ('E = ' , e)
print ('I = ' , i)
print ('O = ' , o)
print ('U = ' , u)

