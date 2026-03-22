# Escreva um algoritmo para ler o ano atual e o ano de nascimento de uma pessoa.
# Escrever uma mensagem que diga se ela poderá ou não votar este ano.
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
if idade >= 16:
    print("Você pode votar este ano!")
else:
    print("Você não pode votar este ano!")

