# #resolução exercicios recuperação
# #exercicio 1
# valor = int(input("Digite o valor para saque: "))
# notas50 = valor // 50
# sobra = valor % 50

# notas20 = valor // 20
# sobra = valor % 20

# notas10 = valor // 10
# sobra = valor % 10

# if sobra == 0:
#     print("notas de R$50:",notas50)
#     print("notas de R$20:",notas20)
#     print("notas de R$10:",notas10)
# else:
#     print("Valor Inválido")

# #exercicio 2
# aprovado = 0
# excesso = 0
# falta = 0
# for i in range(10):
#     peso = int(input("insira o peso em gramas:  "))
#     if peso > 145 and peso < 155:
#         print("aprovado")
#         aprovado += 1
#     elif peso < 145:
#         print("refugada por falta de material")
#         falta += 1
#     else:
#         print("refugada por excesso")
#         excesso += 1
# print(f"total de peças aprovadas: {aprovado}")
# print(f"total de peças refugada por falta de material: {falta}")
# print(f"total de peças refugada por excesso: {excesso}") 

# #exercicio 3
# usuario_correto = "admin123"
# senha_correto = 2026
# contador = 0
# while True:
#     usuario = input("digite o usuario: ")
#     senha = int(input("digite a senha: "))
#     if usuario != usuario_correto and senha != senha_correto:
#         contador +=1 
#     elif usuario == usuario_correto and senha == senha_correto:
#         print("Acesso Concedido")
#         break
#     if contador == 3:
#         print("Conta Bloqueada: Procure o Suporte")
#         break

# exercicio 4
qtd_saltos = int(input("digite quantos saltos: "))
maior = 0 
menor = 0 

for i in range(1,qtd_saltos +1):
    distancia = float(input("digite a distancia: "))
    if i == 1:
        maior = distancia
        menor = distancia
    else:
        if distancia > maior:
            maior = distancia

        if distancia < menor:
            menor = distancia
    media = maior - menor

print("O maior valor é:",maior)
print("O menor valor é:",menor)
print("O intervalo é: ",media)


