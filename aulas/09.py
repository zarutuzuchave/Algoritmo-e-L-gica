#lista
notas = [0.0, 0.0, 0.0, 0.0]
qtd_alunos = 4
alunos_acima = 0
soma_notas = 0
for i in range(qtd_alunos):
    notas[i] = float(input(f"Insira a nota do aluno {i +1}: "))
    soma_notas += notas[i]
media = soma_notas / qtd_alunos
print(f"A media da turma foi {media:.2f}")
for i in range(qtd_alunos):
    if notas[i] >= media:
        alunos_acima += 1
    else:
        alunos_abaixo += 1
print("Alunos acima: ",alunos_acima)
print("Alunos abaixo: ", alunos_abaixo)    

#Carrinho de compras
carrinho = []
while True:
    produto = input("Informe o nome do produto ou sair: ")
    #.lower deixa tudo minusculo
    #.upper deixa em maiusculo
    if produto.lower() == "sair":
        break
    carrinho.append(produto) # append() insere os dados na lista na ultima posição
print(f"----------Itens no seu carrinho: ----------------")
#len() mostra o tamanho da lista
tamanho_carrinho = len(carrinho)
for i in range(tamanho_carrinho):#percorre pelo indice 
    print(f"Posição [{i}] --> Produto: {carrinho [i]}")




