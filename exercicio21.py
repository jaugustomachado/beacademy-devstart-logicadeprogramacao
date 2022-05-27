#Algoritmo "nome esenha do - while"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que permita ao usuário tentar logar
# em seu Sistema informando seu nome e senha. Repita a
# operação até que o nome e senha correspondam a um
# valor armazenado(Marcos – 1234). Caso o usuário
# digite -1 interrompa a repetição e informe que o
# programa será finalizado por solicitação do usuário.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022


teste=True

while teste==True:
    print("digite seu nome de usuário")
    nome=input()
    if nome=="-1":
        print("programa encerrado por solicitação do usuário")
        teste==False
        break
    print("digite sua senha")
    senha=input()
    if senha=="-1":
        print("programa encerrado por solicitação do usuário")
        teste==False
        break
    if nome=='Marcos' and senha=="1234":
        print("bem vindo")
        teste==False
        break