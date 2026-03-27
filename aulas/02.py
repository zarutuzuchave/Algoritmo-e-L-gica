#for e while
i = 1
while i <= 10:
    print("Iteração", i)
    i += 1

i = j = 1
while i <= 10:
    while j <= 10:
        print("Iteração", i,"e", j)
        j += 1
    i += 1
    j = 1

 
while i <= 10:
    print(i)
    i += 1 
    if i == 4:
        break    


i = 0 
while i <= 10:
    i += 1 
    if i == 5:
        continue
    print("Iteração", i)


while True:
    opcao = input("Digite uma opção: ")
    match opcao:
        case "":
            print("Comando vazio...Tentando novamente")
        case "novo":
            print("Novo documento")
        case "salvar":
            print("Documento salvo")
        case "editar":
            print("Editar documento")
        case "sair":
            break
        case _:
            print("Opção inválida")
#exercícios:
#1ex
i = 0
while i <= 19:
    print(i)
    i  += 1
   

#2ex
i = 13
while i <= 25:
    print(i)
    i += 1
#3ex
i = 0    
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

#4ex
i = 0
soma = 0
while i <= 100:
    if i % 2 == 0:
        soma += i
    i += 1

print(soma)
#5ex
i = 0    
while i <= 30:
    if i % 2 != 0:
        print(i)
    i += 1
#6ex    
num = int(input("Digite um número: "))
i = 0
while i <= 9:
    i += 1
    print(num * i)
