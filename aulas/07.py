def escrever():
    print("estou escrevendo...")
    imprimir()
def imprimir():
    print("AnA")
for _ in range(10):
    escrever()

def contar(numero): # =>argumento
    resultado = numero * 10
    return resultado
for i in range(10):
    retorno = contar(i)
    print(retorno)

    


