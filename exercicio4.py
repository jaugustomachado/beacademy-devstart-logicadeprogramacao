#Algoritmo "nome_peso_altura_ICM"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa faz o input do nome, peso e altura do usuário e calcula o IMC
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

print("Qual o seu nome: ")
nome=input()
print("Qual o seu peso: ")
peso=float(input())
print("Qual sua altura: ")
altura=float(input())

print("Seu nome é ", nome, " você tem ",peso, "Kg e tem ", altura, "m de altura. ")
#//Cálculo do IMC
imc = peso/(altura*altura)
print("Seu ICM é de ",round(imc,2))