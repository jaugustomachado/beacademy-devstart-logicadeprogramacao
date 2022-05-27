#Algoritmo "idade do - while"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : Solicitar a idade de várias pessoas e imprimir:
# • Total de pessoas com menos de 18 anos.
# • Total de pessoas com mais de 60 anos.
# • O programa termina quando idade for =-99
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

idade=int(input("informe a idade para pesquisa: "))
jovens=0
idoso=0

while(idade!=-99):
    if idade< 18:
        jovens=jovens+1
        
    elif idade>60:
        idoso=idoso+1
    
    idade=int(input("informe a idade para pesquisa: "))
print("quantidade de jovens:",jovens)
print("quantidade de idosos: ", idoso)