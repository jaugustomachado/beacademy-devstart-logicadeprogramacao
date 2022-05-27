#Algoritmo "produto e preço vetor"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : 
# Faça um programa que solicite ao usuário o
# nome e o preço de 10 produtos e armazene-os
# em um vetor. Ao final imprima o nome e os
# valores correspondentes dos produtos.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

nome=[]
preco=[]

for x in range(10):
    nome.append(input("informe o nome do produto: "))
    preco.append(float(input("informe o preço do produto: ")))
for x in range(10):
    print(nome[x],preco[x])