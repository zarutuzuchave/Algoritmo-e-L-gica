# dia = "segunda-feira"
# match dia: 
#     case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
#         print("Tem aula")
#     case "sábado" | "domingo":
#         print("Não tem aula")
#     case _: #valor curinga, ou seja, se não for nenhum dos casos anteriores
#         print("informe um dia válido")

# opcao = input("Insira a opção desejada: ")

# match opcao:
#     case "novo":
#         print("Novo documento")
#     case "salvar":
#         print("Documento salvo")
#     case "editar": 
#         print("Editar documento")
#     case _: 
#         print("Opção inválida")



numero = int(input("Digite um número: "))
match numero:
    case n if n < 100:
        print("Número negativo")
    case n if n % 2 == 0:
        print("Número par positivo")
    case n:
        print(f"{n} é um número positivo e ímpar")

idade =  input("Digite sua idade: ")
match idade:
    case i if i >= 5 and i <= 7:
        print("Sua categoria é infantil ")
    case i if i >= 8 and i <= 10:
        print("Sua categoria é juvenil")
    case i if i >= 11 and i <= 15:
        print("Sua categoria é adolescente")
    case i if i >= 16 and i <= 30:
        print("Sua categoria é adulto")
    case i if i > 30:
        print("Sua categoria é sênior")            
    case _:
        print("Idade inválida")

if idade >= 5 and idade <= 7:
    print("Sua categoria é infantil ")
elif idade >= 8 and idade <= 10:
    print("Sua categoria é juvenil")
elif idade >= 11 and idade <= 15:
    print("Sua categoria é adolescente")
elif idade >= 16 and idade <= 30:
    print("Sua categoria é adulto")
elif idade > 30:
    print("Sua categoria é sênior")
else:   
    print("Idade inválida")


codOrigem = input("Digite o código de origem: ")
match codOrigem:
    case "1":
        print("Sul")
    case "2":
        print("Norte")
    case "3":
        print("Leste")
    case "4":
        print("Oeste")
    case "5" | "6":
        print("Nordeste")
    case "7" | "8" | "9":
        print("Sudeste")
    case i if i >= "10" and i <= "20":
        print("Centro-Oeste")
    case c if c >= "21" and c <= "30":
        print("Noroeste")
    case _:
        print("Código de origem inválido")
