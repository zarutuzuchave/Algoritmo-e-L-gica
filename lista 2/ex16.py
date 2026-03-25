tabPrecos = print(
"""Bilhete unitário ..................................... 1,30
Bilhete duplo ........................................ 2,60
Bilhete de 10 viagens ......................... 12,00""")

tipo = input("Digite o tipo de bilhete (unico, duplo ou 10 viagens): ")
valorPago = float(input("Digite o valor a ser pago: "))

match (valorPago, tipo):
    case (v, t) if v < 1.30 and t == "unico":
        print("Valor insuficiente para comprar um bilhete unico")
    case (v, t) if v >= 1.30 and v < 2.60 and t == "unico":
        troco = v - 1.30
        print(f"Você comprou um bilhete unitário e tem troco de R$ {troco:.2f}")
    case (v, t) if v >= 2.60 and v < 12.00 and t == "duplo":
        troco = v - 2.60
        print(f"Você comprou um bilhete duplo e tem troco de R$ {troco:.2f}")
    case (v, t) if v >= 12.00 and t == "10 viagens":
        x = int(v // 12.00)
        troco = v - (x * 12.00)
        print(f"Você comprou {x} bilhete de 10 viagens e tem troco de R$ {troco:.2f}")
    case _:
        print("Valor ou tipo de bilhete inválido")







