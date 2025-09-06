import os
os.system("cls || clear")

nome = input("Digite o seu nome: ")
sexo = input("Digite seu sexo (M se for masculino e F se for feminino): ")
estado_civil = input("Digite o seu estado civil (Solteiro(a), Casado(a), Separado(a), Divorciado(a) ou Viúvo(a)): ")

if sexo == "F" and estado_civil == "Casada":
    tempo = input("Quanto tempo de casada você tem (em anos): ")
    print(f"\nNome: {nome}\nSexo: {sexo}\nEstado civil: {estado_civil}\nTempo de casada: {tempo} anos")
else:
    print(f"\nNome: {nome}\nSexo: {sexo}\nEstado civil: {estado_civil}")
