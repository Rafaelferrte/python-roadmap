# Uma variável que pode armazenar multiplos valores

# Lista
frutas = ["maçã", "melancia","uva","banana","pessego"]
# dir(frutas)
# help(frutas)
len(frutas)
"maçã" in frutas

frutas[4] = "cocô"
frutas.append("laranja")
frutas.remove("laranja")
frutas.insert(0, "toranja")
frutas.sort()
frutas.reverse()
frutas.clear()
frutas.index("melancia")


print(frutas[0])
print(frutas[0:4])

for fruta in frutas:
    print(fruta)


# Set
carros = {"BMW", "Audi", "Porsche", "Honda"}
len(carros)
"Audi" in carros
carros.add("Toyota")
carros.remove("Porsche")
carros.pop()
carros.clear()


# Tuple
comidas = ("strogonoff", "pastel","lasanha","kibe")
len(comidas)
"pastel" in comidas
comidas.index("kibe")
comidas.count("lasanha")

for comida in comidas:
    print(comida)