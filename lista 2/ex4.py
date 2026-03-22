# Faça um algoritmo que leia 3 números e imprima os 2 menores deles
numeros = []
for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
print(f"Os 2 menores números são: {sorted(numeros)[:2]}")