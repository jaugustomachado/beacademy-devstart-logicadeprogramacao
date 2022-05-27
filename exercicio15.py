#Algoritmo "múltiplos de 3 entre dois números digitados pelo usuário."
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que imprime os múltiplos de 3 entre dois 
# números digitados pelo usuário.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022")

print("informe dois numeros inteiros para definir o intervalo e obter a lista de multiplos de 3 entre eles")

num1=int(input())
num2=int(input())

for x in range(num1,num2):
    if x%3==0:
        print(x)