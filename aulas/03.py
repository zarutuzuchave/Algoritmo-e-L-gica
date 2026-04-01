#exemplo 1
for i in range(0,10,2):
    print (i)
#exemplo 2
for j in range(10,0,-1):
    print(j)
#exemplo 3
for k in range(0,10):
    print(k)    
#exemplo 4
for _ in range(0,10):
    print("Oi")
#exemplo 5
n = 5
for i in range(n // 2):
    print(i)
#exemplo 6
for i in range(11):
    for y in range(11):
        print(f"{i} x {y} = {i*y}")
#exemplo 7 
for m in range(10):
    print(m)
else:
    print("Fim")
#exemplo 8
for h in range(10):
    print(h)
    if h == 5:
        break
#exemplo 9 
for g in range(10):
    if g == 5:
        continue
    print("iteração",g)

# # exercicios:
# 1. Faça com que um usuário entre com dez números. Após o
# usuário inserir o número apresente esse número pra ele.
# 2. Faça um programa em Python que some os números pares
# no intervalo de 0 a 100.
# 3. Faça um programa em Python que some os 30 primeiros
# números ímpares, e imprima o resultado.
# 4. Faça um programa em Python que apresente a tabuada de
# um valor informado pelo usuário.

#ex1 
for i in range(11):
    num = int(input("Digite um número: "))
    print(num)
#ex2
soma = 0 
for i in range(101):
    if i % 2 == 0:
        soma += i
print(soma)
#ex3
soma = 0
for i in range(60):
    if i % 2 != 0:
        soma += i  
print(soma)
#ex4
num = int(input("Digite um número: "))
for i in range(11):
    print(f"{num} x {i} = {num*i}") 
