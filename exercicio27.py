#Algoritmo "clientes vetor"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : 
#Crie um programa que permita ao usuário
#cadastrar 5 clientes com os seguintes dados:
#• Nome;
#• CPF;
#• RG;
#• Endereço; e
#• Telefone.
# Guarde os dados dos clientes em um vetor e
#ao final exiba-os.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022
nome=[]
cpf=[]
rg=[]
endereco=[]
telefone=[]

for x in range(5):
    nome.append(input("informe o nome: "))
    cpf.append(input("informe o cpf: "))
    rg.append(input("informe o rg: "))
    endereco.append(input("informe o endereco: "))
    telefone.append(input("informe o telefone: "))
for x in range(5):
    print(nome[x],cpf[x],rg[x],endereco[x],telefone[x])
    