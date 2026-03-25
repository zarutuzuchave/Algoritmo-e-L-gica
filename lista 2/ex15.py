#  Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média
# aritmética e a mensagem que segue a tabela abaixo. Para alunos de exame,
# calcule e mostre a nota mínima a ser tirada no exame para que o aluno obtenha
# aprovação, considerando que a média no exame é 6,0.
# Média Ponderada Conceito
# 0,0 |⎯ 3,0 Reprovado
# 3,0 |⎯ 7,0 Exame
# 7,0 |⎯| 10,0 Aprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
match media:
    case m if m >= 0 and m < 3:
        print("Reprovado")
    case m if m >= 3 and m < 7:
        nota_exame = 6 - media
        print(f"Exame. Nota mínima para aprovação: {nota_exame:.2f}")
    case m if m >= 7 and m <= 10:
        print("Aprovado")
        
