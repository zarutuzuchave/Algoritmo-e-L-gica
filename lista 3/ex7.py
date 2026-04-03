# 7. Faça um algoritmo utilizando a Linguagem de Programação Python que faça a soma
# dos n primeiros números primos naturais e apresente o resultado na tela.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True 
n = int(input("Digite um número inteiro positivo: "))
soma = 0
count = 0
num = 2
while count < n:
    if is_prime(num):
        soma += num
        count += 1
    num += 1
print(f"A soma dos {n} primeiros números primos é: {soma}")
