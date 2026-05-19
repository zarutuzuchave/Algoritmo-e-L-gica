# 1. Crie um programa que exiba um menu interativo para o usuário com
# opções de conversão de medidas.
# O programa deve rodar continuamente até que o usuário escolha a
# opção de sair.
# O menu deve ter 3 opções: Converter Celsius para Fahrenheit,
# Converter Metros para Centímetros e Sair.
# Crie uma função específica para cada cálculo de conversão.
# Se o usuário digitar uma opção que não existe, o programa deve
# avisar que a opção é inválida e mostrar o menu novamente

def celsius():
    while True:
        converter = input("Deseja converter Celsius para Fahrenheit?  S/N  "  )
        if converter == "S" or converter == "s":
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 9 /5) + 32
            print(fahrenheit)
        else:
            menu()
        if converter != "S" or converter != "N" or converter != "n" or converter != "s":
                print("opção invalida")
                break
def metros():
    while True:
        cent = input("Deseja converter Metros para Centimetros?  S/N  "  )
        if cent == "S" or cent == "s":
            metros = int(input("Digite os Metros:  "))
            centimetros = metros * 100
            print(centimetros)
        else:
            menu()
        if cent != "S" or cent != "N" or cent != "n" or cent != "s":
                print("opção invalida")
                break
def sair():
    while True:
        sair = input("Deseja sair?   S/N ")
        if sair == "s" or sair == "S":
            break
        else:
            menu()
        if sair != "S" or sair != "N" or sair != "n" or sair != "s":
            print("opção invalida")
            break
def menu():
    print("------------------------------ Bem-Vindo --------------------------------") 
    print("-------------------- Menu para conversão de Medidas ----------------------")
    print("------------------- Converter Celsius para Fahrenheit--------------------- ")
    print("------------------- Converter Metros para Centimetros --------------------- ")
    print("-------------------------------- Sair -------------------------------------- ")

               
menu()
celsius()
metros()
sair()
