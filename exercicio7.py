#Algoritmo "idade"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : o programa pergunta idade ao usuário depois faz informa se o mesmo é
# menor de idade, adulto ou idoso
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022
  
print("Digite sua idade: ")
idade=int(input())

if idade <18 :
    print("Você é menor de idade")
elif(idade < 60):
    print("Você é adulto")
else:
    print("Você é idoso")