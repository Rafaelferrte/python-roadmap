import random 
 
opcoes = ("pedra","papel","tesoura")
jogador= None
computador = random.choice(opcoes)

while jogador not in opcoes:
    jogador = input("Selecione uma opção (pedra, papel, tesoura): ")

print(f"Jogador: {jogador}")
print(f"Computador: {computador}")

if jogador == computador:
    print("Empate!")
elif jogador == "pedra" and computador == "tesoura":
    print("Venceu!")
elif jogador == "papel" and computador == "rock":
    print("Venceu!")
elif jogador == "tesoura" and computador == "paper":
    print("Venceu!")
else:
    print("Perdeu!")