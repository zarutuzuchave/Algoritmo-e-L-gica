def mostrar_disciplina(): #nome de função é sempre um verbo 
    print("Disciplina: Algoritmo e Lógica") 

mostrar_disciplina() # / para chamar a função é só colocar o nome da função e ()

def mostrar_disciplina(nome_disciplina,curso):
    print(f"Disciplina: {nome_disciplina}! Curso: {curso}")
mostrar_disciplina("Algoritmo e Lógica","Sistemas de Informação")

def somar():
    valor1 = input("Digite um valor 1: ") #valor1 é uma variável local, só existe dentro da função
    valor2 = input("Digite um valor 2: ")
    resultado = valor1 + valor2
    print(resultado)
somar()

def realizar_prova(tentativas=3,tempo=30): #defino valor padrão para os parâmetros, caso o usuário não informe um valor, ele usará o valor padrão
    print(f"Você tem {tentativas} tentativas e {tempo} minutos para realizar a prova.")
realizar_prova() #chama a função sem passar parâmetros, então usará os valores padrão
realizar_prova(2) #chama a função passando apenas o valor de tentativas, então usará o valor informado para tentativas e o valor padrão para tempo
realizar_prova(5,60) #chama a função passando parâmetros, então usará os valores informados

def calcular_dobro(n: int) -> int: #defino o tipo do parâmetro e o tipo do retorno da função, isso é opcional, mas ajuda a entender melhor o código
    return n * 2 #return é usado para retornar um valor, ou seja, a função pode ser usada como uma expressão, por exemplo: resultado = calcular_dobro(5)
resultado = calcular_dobro(20)
print(f"O dobro é {resultado}")
