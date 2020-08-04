#Implemente um sistema de uma máquina de trocos, onde o usuario fornece quantas moedas existem disponíveis no estoque.
#Priorizando as menores notas, o sistema deverá calcular o troco para dar ao cliente.


moeda1Real= (int(input('Forneça a quantidade de moedas de 1 real disponiveis: ')))
moeda50Cent= (int(input('Forneça a quantidade de moedas de 50 centavos disponiveis: ')))
moeda25Cent= (int(input('Forneça a quantidade de moedas de 25 centavos disponiveis: ')))
moeda10Cent= (int(input('Forneça a quantidade de moedas de 10 centavos disponiveis: ')))
moeda5Cent= (int(input('Forneca a quantidade de moedas de 5 centavos disponiveis:  ')))
troco1Real= 0
troco50Cent= 0
troco25Cent= 0
troco10Cent= 0
troco5Cent= 0

while True:
    valorGasto= (float(input('digite o valor gasto pelo cliente: ')))
    valorPago= (float(input('digite o valor pago pelo cliente: ')))
    trocoDev= valorPago - valorGasto
    while trocoDev > 0.99 and moeda1Real>0.99:
        trocoDev= trocoDev -1
        moeda1Real= moeda1Real - 1
        troco1Real = troco1Real + 1


    while trocoDev>=0.50 and moeda50Cent>0.99:
        trocoDev = trocoDev - 0.50
        moeda50Cent= moeda50Cent - 1
        troco50Cent = troco50Cent + 1


    while trocoDev>=0.25 and moeda25Cent>0.99:
        trocoDev = trocoDev - 0.25
        moeda25Cent = moeda25Cent - 1
        troco25Cent= troco25Cent + 1


    while trocoDev>=0.10 and moeda10Cent>0.99:
        trocoDev = trocoDev - 0.10
        moeda10cent = moeda10Cent - 1
        troco10Cent = troco10Cent + 1

    while trocoDev>=0.05 and moeda5Cent>0.99:
        trocoDev = trocoDev - 0.05
        moeda5Cent= moeda5Cent - 1
        troco5Cent= troco5Cent +1
    print('O cliente recebera',(troco1Real), 'moedas de 1 real,', (troco50Cent), 'moedas de 50 centavos,', (troco25Cent),' moedas de 25 centavos,', (troco10Cent),'moedas de 10 centavos, e ', (troco5Cent), 'moedas de 5 centavos.')

