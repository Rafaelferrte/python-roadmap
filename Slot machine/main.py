import random

def spin_row():
    simbolos = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(simbolos) for _ in range(3)]    
    

def mostrar_linha(linha):
    print("*************")
    print(" ".join(linha))
    print("*************") 

def receber_pagamento(linha,bet):
    if linha[0] == linha[1] == linha[2]:
        if linha[0] == '🍒':
            return bet * 3
        elif linha[0] == '🍉':
            return bet * 4
        elif linha[0] == '🍋':
            return bet * 5
        elif linha[0] == '🔔':
            return bet * 10
        elif linha[0] == '⭐':
            return bet * 20
        
    return 0

def main():
    balanco = 100

    print("**************************")
    print("Bem Vindo ao Python Slots ")
    print("Simbolos: 🍒 🍉 🍋 🔔 ⭐")
    print("**************************")

    while balanco > 0:
        print(f"Saldo atual: R${balanco}")

        bet = input("Faça sua aposta: ")

        if not bet.isdigit():
            print("Por favor, digite um número válido")
            continue

        bet = int(bet)

        if bet > balanco:
            print("Saldo insuficiente")
            continue

        if bet <= 0:
            print("Bet deve ser maior que 0")
            continue

        balanco -= bet

        linha = spin_row()
        print("Spinning...\n")
        mostrar_linha(linha)

        pagamento = receber_pagamento(linha, bet)

        if pagamento > 0:
            print(f"Você ganhou R${pagamento}")
        else:
            print("Desculpe você perdeu este round")

        balanco += pagamento

        jogar_de_novo = input("Você quer jogar de novo? (Y/N):").upper()

        if jogar_de_novo != 'Y':
            break

    print('********************************')
    print(f'Acabou! Seu balanço final é R${balanco}')


if __name__ == '__main__':
    main()
    