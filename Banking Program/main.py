def mostrar_balanco(balanco):
    print("\n***************************")
    print(f"Seu balanço é R${balanco:.2f}")
    print("***************************\n")
def depositar():
    print("\n***************************")
    quantia = float(input("Digite uma quantia para ser depositada: "))
    print("***************************")

    if quantia < 0:
        print("\n***************************")
        print("Quantia inválida!")
        print("***************************\n")
        return 0
    else:
        return quantia

def sacar(balanco):
    print("\n***************************")
    quantia = float(input("Digite um quantia para ser sacada: "))
    print("***************************\n")

    if quantia > balanco:
        print("\n***************************")
        print("Saldo insuficiente!")
        print("***************************\n")
        return 0
    elif quantia < 0:
        print("\n***************************")
        print("Quantia precisa ser maior que zero")
        print("***************************\n")
        return 0
    else:
        return quantia


def main():
    balanco = 0
    is_running = True

    while is_running:
        print("\n***************************")
        print("     Programa Bancário     ")
        print("***************************\n")
        print("1.Mostrar Balanço")
        print("2.Depositar")
        print("3.Sacar")
        print("4.Sair")
        print("\n***************************\n")
        escolha = input("Digite a sua escolha (1-4):")

        if escolha == "1":
            mostrar_balanco(balanco)
        elif escolha == "2":
            balanco += depositar()
        elif escolha == "3":
            balanco -= sacar(balanco)
        elif escolha == "4":
            is_running = False
        else:
            print("\n***************************")
            print("Escolha inválida!")
            print("***************************\n")
    print("\n***************************")
    print("Obrigado! Tenha um bom dia!")
    print("***************************\n")

if __name__ == '__main__':
    main()