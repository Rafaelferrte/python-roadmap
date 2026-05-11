comidas = []
precos = []
total = 0

while True:
    comida = input("Digite uma comida para comprar (q para sair): ")
    if comida.lower() == "q":
        break
    else:
        preco = float(input(f"Digite o preço do {comida}: R$"))
        comidas.append(comida)
        precos.append(preco)

print("\n----- SEU CARRINHO -----\n")

for comida in comidas:
    print(f"A comida {comida} custa R${precos[comidas.index(comida)]:.2f}")

for preco in precos:
    total += preco

print(f"Seu total é: R${total:.2f}")