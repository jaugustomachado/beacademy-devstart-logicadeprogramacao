#Algoritmo "saldo - while"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : 
# Crie um programa inicie o saldo do cliente com R$ 1000,00
# e que permita o saques consecutivos no valor
# de R$ 150.00 até que seu saldo seja positivo.
# • Quando isto ocorrer interrompa a operação e informe
# que o saque não pode ser efetuado em razão de que o
# saldo era insuficiente para efetuar a operação
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

saldo = 1000
while saldo>0:
    saldo=saldo-150
    print("saque de 150 reais realizado")
print("o saque não pode ser efetuado em razão de que o saldo era insuficiente para efetuar a operação")