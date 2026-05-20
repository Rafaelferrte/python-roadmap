menu = {"pizza": 3.00,
        "nachos": 4.50,
        "pipoca": 6.00,
        "fritas": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "refri": 3.00,
        "limonada": 4.25}

carrinho = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: R${value}")

print("------------------------")

while True:
    comida = input("Escolha um item (q para sair): ")
    if comida.lower() == "q":
        break
    elif menu.get(comida) is not None:
        carrinho.append(comida)

print("------ SEU PEDIDO ------")
for comida in carrinho:
    total += menu.get(comida)
    print(comida, end=" ")

print()
print(f"Total é: R${total:.2f}")