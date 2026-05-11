capitalInicial = 0
taxa = 0
tempo = 0

while capitalInicial <= 0:
    capitalInicial = float(input("Digite o capital inicial: "))
    if capitalInicial <= 0:
        print("O capital inicial não pode ser menor ou igual a 0")

while taxa <= 0:
    taxa = float(input("Digite a taxa de juros: "))
    if taxa <= 0:
        print("A taxa de juros não pode ser menor ou igual a 0")


while tempo <= 0:
    tempo = int(input("Digite o tempo (anos): "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual a 0")

total = capitalInicial * pow((1 + taxa  / 100),tempo)
print(f"O montante final depois de {tempo} ano/s: R${total:.2f}")


 