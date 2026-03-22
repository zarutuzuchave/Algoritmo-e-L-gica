#  Escreva um algoritmo que leia dois números que deverão ser colocados,
# respectivamente, nas variáveis VA e VB. O algoritmo deve, então, trocar os
# valores de VA por VB e vice-versa e mostrar o conteúdo destas variáveis.
VA = float(input("Digite o valor de VA: "))
VB = float(input("Digite o valor de VB: "))
cod = VA
VA = VB 
VB = cod
print("O valor de VA é:", VA)
print("O valor de VB é:", VB)
