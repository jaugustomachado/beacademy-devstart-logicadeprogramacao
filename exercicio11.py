#Algoritmo "quadrado e triangulo"
#// Logica de programação
#// Marcos Monteiro
#// Descrição   : programa que receba do usuário a 
# figura geométrica que deseja calcular a área e 
# o perímetro (Q-Quadrado ou T-Triângulo) e 
# calcule e exiba a área e o perímetro da figura escolhida.
#// Autor(a)    : José Augusto
#// Data atual  : 25/05/2022

print("Para calcular quadrado digite Q, para traingulo digite T: ")
opcao=input().upper()
if opcao=="Q":
    lado=float(input("informe o lado do quadrado em cm: "))
    area=lado*lado
    perimetro=4*lado
elif opcao== "T":
    base=float(input("Digite a base do triangulo em cm: "))
    altura=float(input("Digite a altura do triangulo em cm: "))
    lado1=float(input("Digite um dos lados do triangulo em cm: "))
    lado2=float(input("Digite o outro lado do triangulo em cm: "))
    area= base *(altura / 2 )
    perimetro= base + lado1 + lado2


print("Area é de ",area,"cm² e o perimetro é de ", perimetro," cm")
