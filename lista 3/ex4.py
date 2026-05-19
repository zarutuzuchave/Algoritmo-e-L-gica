# 4. Faça um programa em Python que receba 10 números e indique quais são maiores que
# 25 e menores que 85.

for i in range(10):
    num = int(input("digite 10 numeros: "))
    if num >= 25 and num <= 85:  
        print(f"o numero está no intervalo")
    else:
        print("Não está no intervalo")
