# Faça uma função que recebe um valor inteiro e verifica se o valor é
# par ou ímpar. A função deve retornar um valor inteiro. 

def verificar_par_impar(valor):
    if valor % 2 == 0:
        return 0   
    else:
        return 1   

numero = int(input("Digite um número inteiro: "))

resultado = verificar_par_impar(numero)

if resultado == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")