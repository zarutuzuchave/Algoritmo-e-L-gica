# 5. Dado as listas A e B de tamanho 6 e do tipo float faça um programa que,
#   utilizando um laço de repetição,e utilizando outro laço, inicialize os valores de ambas
#   as listas, some os valores posição por posição e guarde o novo valor na lista A.

<<<<<<< HEAD
lista_a = []
lista_b = []



for i in range(6):
    lista_a.append(float(input(f"Digite A: ")))
    lista_b.append(float(input(f"Digite B: ")))
for i in range(6):
    lista_a[i] = lista_a[i] + lista_b[i]
    

print(lista_a)
=======
a = []
b = []

for i in range(6):
    a.append(float(input("Digite um valor para A: ")))
for i in range(6):
    b.append(float(input("Digite um valor para B: ")))
for i in range(6):
    a[i] += b[i]
>>>>>>> e0e1d35152e71028541d9aa62b6ee4de73d96190
