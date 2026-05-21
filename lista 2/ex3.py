# Faça um algoritmo que leia 4 números e imprima o menor deles. Use apenas 2
# variáveis no seu algoritmo

num = int(input("Digite o 1º número: "))
menor = num
for i in range(2, 5):
    num = int(input(f"Digite o {i}º número: "))
    if num < menor:
        menor = num
print(f"O menor número é: {menor}")