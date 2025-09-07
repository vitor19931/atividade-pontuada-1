import os
os.system("cls || clear")

renda = float(input("Digite sua renda: R$ "))
valor_emprestimo = float(input("Digite o valor do emprestimo: "))
num_prestacao = int(input("Digite o número de prestações: "))

prestacao = valor_emprestimo / num_prestacao

if valor_emprestimo <= renda * 10 and prestacao <= renda * 0.3:
    print("o senhor(a) pode receber o emprestimo pode ser recebido")
else:
    print("Infelizmente o senhor(a) não pode receber o emprestimo")    