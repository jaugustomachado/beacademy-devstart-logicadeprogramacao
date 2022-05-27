#Algoritmo "IMC"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : rograma que recebe a altura e o peso da pessoa e a classifica em grupos
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022


print("Qual o seu peso: ")
peso=float(input())
print("Qual sua altura: ")
altura=float(input())

imc=altura/peso^2

if imc<19:
    print("Abaixo do peso")
elif imc>=19 and imc<25:
    print("Peso normal")
elif imc>=25 and imc<30:
    print("Sobrepeso")
elif imc>=30 and imc<40:
    print("Obesidade tipo 1")
else:
    print("Obesidade Mórbida")