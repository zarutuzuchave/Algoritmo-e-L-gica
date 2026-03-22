# Faça um programa que apresente o quadrado de todo número par que ele recebe.
# Exemplo: Entrada: 8 - Processamento: é par? Então imprima 8x8 - Saída: 64
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é: {quadrado}")
else:
    print(numero)
    