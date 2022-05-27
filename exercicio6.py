#Algoritmo "Operadores Aritmeticos"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : o programa pergunta nome e idade ao usuário depois faz o print do 
# resultado booleano da comparação entre as diferentes proposições
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

print("Digite seu nome: ")
nome=input()
print("Digite sua idade: ")
idade=int(input())
print("seu nome é:", nome, "e sua idade é: ", idade)

print("Idade é maior de 18 anos?: ",(idade>=18))
print("Idade é diferente de 25? ",(idade!=25))
print("Idade é diferente de 25 e nome igual a Marcos: ",(idade!=25) and (nome == "Marcos"))
print("Idade é diferente de 25 ou nome igual a Marcos: ", (idade!=25) or (nome == "Marcos"))
print("Idade dividida por 2 é igual a zero: ", idade%2 == 0)