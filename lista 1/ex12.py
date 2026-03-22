# Escreva um algoritmo que converte altura em metros para altura em centímetros,dada a
# relação: 1m = 100 cm. O algoritmo deve solicitar ao usuário que forneça a sua altura em
# metros e deve imprimir a mesma em cm
usuario = float(input("Digite sua altura em metros: "))
altura_cm = usuario * 100
print("Sua altura em centímetros é:", f"{altura_cm:.2f}")