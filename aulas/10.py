number = [2,4,6]
# for i in range(len(number)):
#     print(number)

bicletas = ["trek","cannondale","redline","specialized"]
# for bicicleta in bicletas:
#     print (bicicleta)
print(bicletas[-2])# print a posição -2 da lista

print(bicletas[-2].title())# mostra como um titulo

bicletas.insert(2,"teste")# insere em uma posiçao especifica 
print(bicletas)

# del bicletas[-1] # deleta da lista na 

bicletas_popped = bicletas.pop()# remove do fim da lista e adiciona nessa variavel

print(bicletas)
print(bicletas_popped)

bicletas_popped = bicletas.pop(1)# remove da posicao 1 e adiciona nessa variavel

bicletas.remove("redline")# remove pelo elemento

print(max(number)) # pega o maior valor
print(min(number)) # pega o menor
print(sum(number)) # soma todos os valores da lista

nomes = ["Ana","Ronaldo","Filipe"] 

