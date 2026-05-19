# 7. Faça um algoritmo utilizando a Linguagem de Programação Python que faça a soma
# dos n primeiros números primos naturais e apresente o resultado na tela.


primos = 0
while True:
    num = int(input("digite numeros naturais ou 0 para sair : "))
    if num <= 0:
        break
    if num % 2 == 0:
        primos += num
    print(f"Soma dos numeros primos: {primos}")


