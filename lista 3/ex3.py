# 3. Faça um programa em Python que leia cinco valores: a, b, c, d e e, todos números
# inteiros, e mostre-os em ordem crescente e decrescente.


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
e = int(input("Digite o valor de e: "))

for i in range(5):

    if a > b:
        a, b = b, a

    if b > c:
        b, c = c, b

    if c > d:
        c, d = d, c

    if d > e:
        d, e = e, d


print("\nOrdem crescente:")
print(a, b, c, d, e)
print("\nOrdem decrescente:")
print(e, d, c, b, a)