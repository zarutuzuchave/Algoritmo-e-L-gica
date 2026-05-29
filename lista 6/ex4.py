# 4. Dado uma lista A de tamanho 8 e do tipo inteiro faça um programa em Python que,
# utilizando um laço de repetição, receba os valores de entrada e, utilizando outro laço
# de repetição, verifique qual o maior valor da lista e apresente esse valor.
lista = []
for i in range(8):
    entrada = int(input("digite os valores de entrada: "))
    lista.append(entrada)
maior = lista[0]
for i in range(8):
    if lista[i]> maior:
        maior = lista
    print(maior)


