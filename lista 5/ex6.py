def converter_tempo(segundos):

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    print(horas, "horas")
    print(minutos, "minutos")
    print(segundos_restantes, "segundos")


tempo = int(input("Digite o tempo em segundos: "))

converter_tempo(tempo)