# Faça um algoritmo que leia 3 números e imprima os 2 menores deles

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))


if num1 < num2 and num1 < num3 and num2 < num3:
    print(f"Os 2 menores números são: {num1} e {num2}")
elif num2 < num1 and num2 < num3 and num1 < num3:
    print(f"Os 2 menores números são: {num2} e {num1}")
else:
    print(f"Os 2 menores números são: {num3} e {num1}")
