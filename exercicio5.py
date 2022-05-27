#Algoritmo "deposito e saldo"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa faz o print da quantia inicial em conta (200,00)
# pergunta quanto o usuário que depositar e adiciona no saldo total.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

print("Seu saldo atual é de R$ 200,00")
print("Quanto deseja depositar: R$ ")
deposito=float(input())
print("Saldo inicial: R$ 200")
print("Depositado: R$ ",deposito)
print("Saldo atualizado: R$ ",(200 + deposito))