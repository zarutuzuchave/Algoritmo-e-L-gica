# Uma pessoa é obrigada a realizar o alistamento no exército brasileiro se for do
# sexo masculino e tiver 18 anos. Faça um programa que verifique se o usuário do
# seu programa precisará passar pelo processo de alistamento ou não.
usuario = input("Digite o nome do usuário: ")
sexo = input("Digite o sexo do usuário: (m/f) ")
idade = int(input("Digite a idade do usuário: "))
alistado = input("O usuário já se alistou?: (s/n)")
if sexo == 'm' and idade >= 18 and alistado == 'n':
    print(f"{usuario}, você precisa se alistar no exército brasileiro.")    
else:
    print(f"{usuario}, você não precisa se alistar no exército brasileiro.")
