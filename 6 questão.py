import os
os.system("cls || clear")

nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))


media = (nota1 + nota2) /2


if media >=6:
    print("Parabens você passou")
elif media >= 4.1 and media <= 5.9:
    print("O aluno foi para recuperação")
else:
    print("o aluno foi reprovado")  

