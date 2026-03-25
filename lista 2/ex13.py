# Faça um algoritmo equivalente ao último exercício, isto é, que leia 5 números e
# imprima quantos números são maiores que 100, quantos números são menores
# que 17 e quantos números são menores que 17 e maiores que 100. 
contador = 0
contador_menor_17 = 0
contador_entre_17_e_100 = 0
for _ in range(5):
    numero = int(input("Digite um número: "))
    if numero > 100:
        contador += 1
    elif numero < 17:
        contador_menor_17 += 1
    elif 17 <= numero <= 100:
        contador_entre_17_e_100 += 1

print(f"Quantidade de números maiores que 100: {contador}") 
print(f"Quantidade de números menores que 17: {contador_menor_17}")
print(f"Quantidade de números entre 17 e 100: {contador_entre_17_e_100}")