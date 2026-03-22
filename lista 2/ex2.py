# Faça um algoritmo que leia 3 números e imprima o menor deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 < num2 and num1 < num3:
    print("O menor número é o num1: ", num1)
elif num2 < num1 and num2 < num3:
    print("O menor número é o num2: ", num2)
else:
    print("O menor número é o num3: ", num3)
