dobros = []
for x in range(1, 11):
    dobros.append(x * 2)

print(dobros)


triplos = [i * 3 for i in range(1,11)]

print(triplos)

quadrado = [z * z for z in range(1,11)]
print(quadrado)


frutas = ["maçã", "laranja", "banana", "cocô"]
frutas = [fruta.upper() for fruta in frutas]

print(frutas)

numeros = [1,-2, 3, -4, 5, -6]
numeros_positivos = [num for num in numeros if num >= 0]

