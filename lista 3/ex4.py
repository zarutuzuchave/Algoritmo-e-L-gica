# 4. Faça um programa em Python que receba 10 números e indique quais são maiores que
# 25 e menores que 85.
numeros = []
for i in range(10):
    num = int(input(f"Digite o número {i + 1}: "))
    numeros.append(num)
print("Números maiores que 25 e menores que 85:")
for num in numeros:
    if 25 < num < 85:
        print(num)  
        