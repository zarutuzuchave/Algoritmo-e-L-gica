# Faça um algoritmo que leia 4 números e imprima o menor deles. Use apenas 2
# variáveis no seu algoritmo
numeros = []
for i in range(4):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"O menor número é: {min(numeros)}")