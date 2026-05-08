# Questão 1: Média Salarial
# Foi feita uma pesquisa com 10 trabalhadores na cidade de Três Lagoas para saber a média salarial de uma determinada região da cidade. 
# Faça um programa em Python que receba o salário desses 10 trabalhadores, calcule a média salarial e apresente-a na tela.

# media = 0
# soma = 0
# while media < 10:
#     pesquisa = int(input("digite o salario: "))
#     soma += pesquisa
#     media += 1
#     if media == 10:
#         mediaSalario = soma/media 
# print(mediaSalario)



# Questão 2: Eleição
# Faça um programa em Python que receba um número X de pessoas em uma eleição e verifique se uma pessoa está apta para votar ou não.
# Lembrando-se que:
# - Aos 16 anos um jovem pode optar por votar ou não;
# - Aos 18 anos a pessoa é obrigada a votar;
# - Após os 65 anos, torna-se facultativo a votação.
# Ao final o programa deverá contabilizar a quantidade de pessoas que votaram e a quantidade de pessoas que não votaram.

# PesVotaram = 0
# PesNvotaram = 0

# while True:
#     idade = int(input("digite sua idade ou -1 para sair: "))
#     if idade == -1:
#         break
#     if idade == 16 or idade == 17 or idade >= 65:
#         resposta = input("Você deseja votar? (s/n): ")
#         if resposta == 's' or resposta == 'sim':
#             PesVotaram += 1
#         else:
#             PesNvotaram += 1
#     elif idade >= 18 and idade < 65:
#         PesVotaram += 1
#     else:
#         break
# print(f"Quantidade de pessoas que votaram: {PesVotaram}")
# print(f"Quantidade de pessoas que não votaram: {PesNvotaram}")

# Questão 3: Tabuada
# Faça um programa em Python em que o usuário informe um número para calcular a sua tabuada.
# Em seguida crie uma função que receba esse número por parâmetro, calcule e mostre a sua tabuada conforme o exemplo abaixo:
# 2 * 1 = 2
# def tabuada(num):
#     for i in range (1,11):
#         print(num, " X ",i,"=" , num * i )
# numero = int(input("Digite um número para calcular a tabuada: "))
# tabuada(numero)

# Questão 4: Idade Nadador
# Faça um procedimento que recebe a idade de um nadador por parâmetro e retorna, também por parâmetro, a categoria desse nadador de acordo com a tabela abaixo:

# Idade       Categoria

# 4 a 6 anos    Infantil A
# 7 a 9 anos    Infantil B
# 10 - 14 anos   Juvenil A
# 15-17 anos     Juvenil B
# Maiores de 18 anos  Adulto

# def Catgoria(idade):
#      if idade >= 4 and idade <= 6:
#          return "Infantil A"
#      elif idade >= 7 and idade <= 9:
#          return "Infantil B"
#      elif idade >= 10 and idade <= 14:
#          return "Juvenil A"
#      elif idade >= 15 and idade <=17:
#          return "Juvenil B"
#      elif idade >= 18:
#          return "Adulto"
#      else:
#          return "Fora da lista"
         
# i = int(input("digite sua idade: "))
# resultado =  Catgoria(i)
# print(f"Sua categoria é: {resultado}")

# Questão 5: Média
# Faça uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.
# def somaPositivos():
#     soma = 0
#     media = 0
#     while True:
#         numerosP = int(input("Digite os numeros ou -1 para parar : "))
#         if numerosP == -1:
#             break 
#         if numerosP > 0: 
#             soma += numerosP
#             media += 1
#     if media > 0:
#         media = soma / media
#     return media


# resultado = somaPositivos()
# print(resultado)

















