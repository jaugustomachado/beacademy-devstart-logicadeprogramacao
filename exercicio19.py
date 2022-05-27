#Algoritmo "TABUADA COM WHILE"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que, imprime a tabuada de um
# número digitado pelo usuário.
# O programa repete a operação,por tantas vezes quanto o usuário desejar
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022")

num=float(input("informe um número para descobrir sua tabuada: "))
cont=0
while(cont<=10):
    print(cont," X ",num," = ",round(cont*num,2))
    cont=cont+1