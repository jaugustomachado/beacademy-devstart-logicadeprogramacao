#Algoritmo "saque"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que recebe um valor de depósito 
# do usuário e atualize o seu saldo. Ao final exibe o 
# valor inicial o depósito e o saldo atual.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

print("Seu saldo atual é de: R$ 100,00, deseja depositar ou sacar? (D/S)")
operacao=input().upper()
if operacao=='D':
    deposito=float(input("informe o valor para depósito:"))
    saldo=float(100+deposito)
    print("O saldo antes da operação era de R$",100)
    print("O valor do deposito foi de R$",deposito)
    print("O saldo final é de R$",saldo)
    saldoInicial=saldo
elif operacao=='S':
    saque=float(input("informe o valor para saque:"))
    saldo=float(100-saque)
    print("O saldo antes da operação de saque era de R$",100)
    print("O valor do saque foi de R$",saque)
    print("O saldo final é de R$",saldo)
    saldoInicial=saldo
print("fim da operação")