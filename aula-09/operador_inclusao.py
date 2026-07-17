palavra = "CACHORRO"

letra = input("Adivinhe uma letra na palavra secreta: ")

if letra in palavra:
    print(f"Há {letra}")
else:
    print(f"{letra} não encontrado")

    
notas = {"Sandy": "A", 
         "Lula molusco": "B", 
         "Bob esponja": "C", 
         "Patrick": "D"}

estudante = input("Digite o nome do estudante: ")

if estudante in notas:
    print(f"{estudante} ficou com nota {notas[estudante]}")
else:
    print(f"{estudante} não encontrado")