#Algoritmo "OPERACOES BANCARIAS"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que,permite ao usuário escolher a operação a 
# realizar (depósito ou saque ou transferência) , caso a
# operação seja de transferência solicite o nome do
# banco, da agência e conta, receba as informações e,
# ao final exiba o valor inicial, a operação realizada 
# e o saldo atual, no caso de transferência exiba
# também os dados do banco, agência e conta.
# O programa repete a operação,por tantas vezes quanto o usuário desejar
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022")

print("bem vindo ao banco, saldo atual é 100,00")
saldo=100
quantidadeOperacoes=int(input("quantas operações quer fazer hoje: "))

for x in range (quantidadeOperacoes):
    transacao=input("qual operação deseja fazer? S-saque, T-transferência, D-depósito: ")
    if transacao.upper()=='S':
        saque=float(input("qual valor deseja sacar? "))
        print("saque de ",saque," realizado com sucesso")
        saldo=saldo-saque
        print("saldo atual é de : ",saldo)
    elif transacao.upper()=='D':
        deposito=float(input("qual valor deseja depositar? "))
        print("deposito de ",deposito," realizado com sucesso")
        saldo=saldo+deposito
        print("saldo atual é de : ",saldo)
    elif transacao.upper() == 'T':
        banco=input("Qual banco conta a receber os valores pertence? ")
        agencia=int(input("digite a agencia sem o digito: "))
        conta=float(input("digite o número da conta com o digito: "))
        transferencia=float(input("informe o valor a ser trasnferido: "))
        print("dados do recebedor: Banco: ",banco,"agencia: ",agencia,"conta: ",conta)
        print("transferência de ",transferencia," realizado com sucesso")
        saldo=saldo-transferencia
        print("saldo atual é de : ",saldo)
    