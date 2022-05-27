#Algoritmo "notas vetor"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : 
# Crie um programa que permita cadastrar os
# seguintes dados de um Aluno: Nome, nota1 e 
# nota2. Receba estes valores em vetores e 
# calcule e exiba ao final todos os dados e a 
# informação se o aluno foi aprovado(media 
# maior ou igual a 6) ou reprovado(media inferior a 6).
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

nome=[]
nota1=[]
nota2=[]
media=[]
cont=0
print("deseja cadastrar notas de aluno? S/N ")
opcao=input().upper()
while opcao=='S':
    print("digite o nome do aluno")
    nome.append(input())
    print("digite a nota1 do aluno")
    nota1.append(float(input()))
    print("digite a nota2 do aluno")
    nota2.append(float(input()))
    med=round((nota1[cont]+nota2[cont])/2,2)
    media.append((med))
        
    print("deseja cadastrar notas de aluno? S/N ")
    opcao=input().upper()
for x in range(len(nome)):
    if media[x]<6:
        print(nome[x], "reprovado")
    else:
        print(nome[x], "aprovado")