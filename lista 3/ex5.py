# 5. Faça um algoritmo utilizando a Linguagem de Programação Python que leia a
# quantidade de números que o usuário desejar digitar e imprima a soma desses valores.

quantidade = int(input("Quantos números você deseja digitar? "))
soma = 0
for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    soma += numero  
print(f"A soma dos números digitados é: {soma}")
