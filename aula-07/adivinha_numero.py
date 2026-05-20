import random

menor_num = 1
maior_num = 100
resposta = random.randint(menor_num, maior_num)
palpites = 0
funcionando = True

print("Jogo de Adivinhar Numero em Python")
print(f"Escolha um número entre {menor_num} - {maior_num}:")

while funcionando:
    palpite = input("Tente acertar o número: ")

    if palpite.isdigit():
        palpite = int(palpite)
        palpites += 1

        if palpite <menor_num or palpite > maior_num:
            print("Esse número está fora do intervalo")
            print(f"Escolha um número entre {menor_num} - {maior_num}:")
        elif palpite < resposta:
            print("Baixo de mais! Tente de novo.")
        elif palpite > resposta:
            print("Alto demais! Tente de novo.")
        else:
            print(f"Correto! A resposta é {resposta}")
            print(f"Número de tentativas: {palpites}")
            funcionando = False

    else:
        print("Resposta Inválida!")
        print(f"Escolha um número entre {menor_num} - {maior_num}:")