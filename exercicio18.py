#Algoritmo "NOME E SENHA"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que solicita ao usuário o seu
# nome e senha do cartão e valide se a senha e
# nome são corretos (Nome: Marcos e senha: 
# paylivre) e, caso positivo, dê boas vindas ao
# usuário e, em caso negativo, solicite os dados
# novamente.
# O programa repete a operação,por tantas vezes quanto o usuário desejar
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022")

print("digite seu nome de usuário")
nome=input()
print("digite sua senha")
senha=input()

while( nome!='Marcos' and senha!="payLivre"):
    print("Usuário ou senha incorretos, favor tentar novamente")
    print("digite seu nome de usuário")
    nome=input()
    print("digite sua senha")
    senha=input() 
if nome=='Marcos' and senha=="payLivre":
    print("boas vindas")