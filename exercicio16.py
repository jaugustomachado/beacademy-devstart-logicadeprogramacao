#Algoritmo "múltiplos de 3 entre dois números digitados pelo usuário."
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que imprime a tabuada de um número informado pelo usuário
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022")


print("informe um numero para descobrir a tabuada dele: ")
num=float(input())
for x in range(11):
    print(x," X ",num," = ",round(x*num,2))
    
    