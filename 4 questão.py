import os
os.system("cls || clear")

morango = float(input("Digite a quantidade de morangos (Kg): "))
maca = float(input("Digite a quantidade de maças (em Kg): "))


#preço morango
if morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

#preço da maça
if maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50            

#total sem desconto
total = (morango * preco_morango) + (maca * preco_maca)

peso_total = morango + maca

if peso_total >= 10 or total > 15:
    total = total * 0.9 #desconto de 10%


print(f"valor a pagar: R$ {total:.2f}")