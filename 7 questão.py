import os
os.system("cls || clear")

produto = (input("Digite o nome do produto: "))
quantidade = int(input("Informe a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitario: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05
    
    
total_pagar = total - desconto    

print(f"Produto: {produto}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")        