import os
os.system("cls || clear")

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

soma = a + b

if a + b < c:
    print("È menor que c")
elif a + b == c:
    print("Numero são iguais")

else:
    print("È maior que c")    