# Para doar sangue uma pessoa precisa ter entre 18 e 69 anos e pesar no mínimo 50 kg.
# Faça um programa que pergunte a idade e o peso do usuário e verifique se
# ele pode doar sangue
usuario = input("Digite o nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))
peso = float(input("Digite o peso do usuário (em kg): "))
if 18 <= idade <= 69 and peso >= 50:
    print(f"{usuario} pode doar sangue.")
else:
    print(f"{usuario} não pode doar sangue.")