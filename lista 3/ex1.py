# 1. Faça um programa em Python que leia um valor inteiro e positivo n, e calcule a
# expressão abaixo. Após, imprima o resultado na tela.
# Soma = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

n = int(input("Digite um número inteiro e positivo: "))
soma = 0
for i in range(1, n + 1):
    soma += 1 / i
print(f"O resultado da soma é: {soma}")
    