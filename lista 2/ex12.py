# Faça um algoritmo que leia 5 números e imprima quantos números menores que
# 17 e maiores que 10 foram digitados. 
counter = 0
for _ in range(5):
    numero = int(input("Digite um número: "))
    if 10 < numero < 17:
        counter += 1
print(f"Quantidade de números; {counter}")