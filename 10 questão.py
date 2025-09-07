import os
os.system("cls || clear")


tipo = input("Digite o tipo de combustível (A para álcool, G para gasolina): ")
litros = float(input("Digite o número de litros vendidos: "))


preco_alcool = 3.79
preco_gasolina = 6.59


match tipo:
    case "A":
        preco = preco_alcool
        desconto = 0.10 if litros <= 25 else 0.20
    case "G":
        preco = preco_gasolina
        desconto = 0.15 if litros <= 25 else 0.30
    case _:
        print("Tipo de combustível inválido!")
      

valor_total = litros * preco * (1 - desconto)

print(f"Valor a pagar: R$ {valor_total:.2f}")
