questoes = ("Qual a capital da Austrália? ",
            "Qual o maior mamifero do mundo? ",
            "Qual gás mais abundante da terra? ",
            "Quantos ossos tem no corpo humano? ",
            "Qual o planeta mais quente do sistema solar? ")

opcoes = (("A. Sydney","B. Melbourne","C. Canberra","D. Brisbane"),
          ("A. Baleia","B. Elefante","C. Girafa","D. Rinoceronte"),
          ("A. Nitrogenio","B. Oxigenio","C. Helio","D. Ozonio"),
          ("A. 206","B. 207","C. 208","D. 209"),
          ("A. Mercurio","B. Venus","C. Terra","D. Marte"))

respostas = ("C","A","A","A","B")
palpites = []
pontuacao = 0
num_questao = 0

for questao in questoes:
    print("-------------------------------")
    print(questao)
    for opcao in opcoes[num_questao]:
        print(opcao)
    
    palpite = input("Digite (A, B, C, D): ").upper()
    palpites.append(palpite)
    if palpite == respostas[num_questao]:
        pontuacao += 1
        print("CORRETO!")
    else:
        print("INCORRETO!")
        print(f"{respostas[num_questao]} é a resposta correta")
    num_questao += 1

print("-------------------------------")
print("           RESULTADO           ")
print("-------------------------------")

print("Respostas: ", end="")
for resposta in respostas:
    print(resposta, end=" ")
print()


print("Palpites: ", end="")
for palpite in palpites:
    print(palpite, end=" ")
print()

pontuacao= int(pontuacao / len(questoes) * 100)
print(f"Sua pontuação é: {pontuacao}%")