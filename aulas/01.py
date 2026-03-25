dia = "segunda-feira"
match dia: 
    case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
        print("Tem aula")
    case "sábado" | "domingo":
        print("Não tem aula")
    case _: #valor curinga, ou seja, se não for nenhum dos casos anteriores
        print("informe um dia válido")

opcao = input("Insira a opção desejada: ")

match opcao:
    case "novo":
        print("Novo documento")
    case "salvar":
        print("Documento salvo")
    case "editar": 
        print("Editar documento")
    case _: 
        print("Opção inválida")

        