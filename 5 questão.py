import os
os.system("cls || clear")


operação = input("Digite a operação (+ - * /): ")
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

match operação:
    case "+":
        resultado = a + b 
    case "-":
        resultado = a - b 
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        resultado = "operação invalida"   
        
print(f"Resultado: {resultado}")        