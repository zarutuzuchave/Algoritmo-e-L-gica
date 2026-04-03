# 6. Faça um algoritmo utilizando a Linguagem de Programação Python que permita ao
# usuário informar a idade de quantas pessoas ele deseja registrar. Em seguida, o
# algoritmo deve apresentar a soma das pessoas maiores de idade e a média de idade
# das pessoas menores de idade informadas.

quantidade = int(input("Quantas pessoas você deseja registrar? "))
soma_maiores = 0
soma_menores = 0
count_menores = 0
for i in range(quantidade):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    if idade >= 18:
        soma_maiores += 1
    else:
        soma_menores += idade
        count_menores += 1

print(f"Quantidade de pessoas maiores de idade: {soma_maiores}")
if count_menores > 0:
    media_menores = soma_menores / count_menores
    print(f"Média de idade das pessoas menores de idade: {media_menores}")
else:
    print("Nenhuma pessoa menor de idade informada.")
    