#Implemente uma calculadora em Python.

def somaValores(valor1,valor2):
    valor = valor1+valor2
    return valor


def divValores(valor1,valor2):
    valor = valor1/valor2
    return valor

def multValores(valor1,valor2):
    valor = valor1*valor2
    return valor

def subtValores(valor1,valor2):
    valor = valor1*valor2
    return valor

n= float(input('digite: '))
n2= float(input('digite: '))
funcao= float(input('digite 1 para soma, 2 para div, 3 para multpl, 4 para subtracao:  '))

if funcao==1:
    valor = somaValores(n,n2)
    print(valor)

if funcao==2:
    valor = divValores(n,n2)
    print(valor)

if funcao==3:
    valor = multValores(n,n2)
    print(valor)

if funcao==4:
    valor = subtValores(n,n2)
    print(valor)

