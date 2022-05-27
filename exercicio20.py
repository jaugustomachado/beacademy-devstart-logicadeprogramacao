#Algoritmo "calculadora com while"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que solicite ao usuário a 
# operação desejada e implemente as quatro
# operações matemáticas (soma, subtração,multiplicação e divisão)
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

print("informe dois numeros")
num1=float(input())
num2=float(input())
opcao=input("deseja fazer alguma operação S/N: ").upper()

while(opcao=='S'):

    operacao=int(input("informe o número da operação: 1(+) 2(-) 3(/) 4(*): "))
    if operacao==1:
        res=num1+num2
        print("resultado da soma: ",res)
    elif operacao==2:
        res=num1-num2
        print("resultado da subtração: ",res)
    elif operacao==3:
        res=num1/num2
        print("resultado da divisão: ",res)
    elif operacao==4:
        res=num1*num2
        print("resultado da multiplicação: ",res)
    else:
        print("opção inexistente")
    opcao=input("deseja fazer alguma operação S/N: ").upper()
print("programa finalizado")
            
        