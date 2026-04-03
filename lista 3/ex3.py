# 3. Faça um programa em Python que leia cinco valores: a, b, c, d e e, todos números
# inteiros, e mostre-os em ordem crescente e decrescente.

numeros = []
for i in range(5):
    num = int(input(f"Digite o número {i + 1}: "))
    numeros.append(num)
numeros.sort()
print("Números em ordem crescente:", numeros)
numeros.sort(reverse=True)
print("Números em ordem decrescente:", numeros)