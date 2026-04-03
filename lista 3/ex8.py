# 8. Dados n e uma sequência de n números inteiros positivos, determinar a soma dos
# números pares, dos ímpares e as respectivas quantidades de cada um dos
# subconjuntos.

n = int(input("Digite o número de elementos na sequência: "))
soma_pares = 0
soma_impares = 0
quantidade_pares = 0
quantidade_impares = 0
for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    else:
        soma_impares += numero
        quantidade_impares += 1
print(f"Soma dos números pares: {soma_pares}")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
