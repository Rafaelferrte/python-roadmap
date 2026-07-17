import random
from listapalavras import words

palavras = ("maçã","laranja","banana","cocô","abacaxi")

arte_forca = {0: ("   ",
                  "   ",
                  "   "), 
              1: (" O ",
                  "   ",
                  "   "), 
              2: (" O ",
                  " | ",
                  "   "), 
              3: (" O ",
                  "/| ",
                  "   "), 
              4: (" O ",
                  "/|\\",
                  "   "), 
              5: (" O ",
                  "/|\\",
                  "/  "), 
              6: (" O ",
                  "/|\\",
                  "/ \\")}


def mostrar_cara(chutes_errados):
    for linha in arte_forca[chutes_errados]:
        print(linha)

def mostrar_dica(dica):
    print(" ".join(dica))

def mostrar_resposta(resposta):
    print(" ".join(resposta))

def main():
    resposta = random.choice(palavras)
    dica = ["_"] * len(resposta)
    chutes_errados = 0
    letras_sugeridas = set()
    is_running = True

    while is_running:
        mostrar_cara(chutes_errados)
        mostrar_dica(dica)
        chute = input("Digite uma letra: ").lower()

        if len(chute) != 1 or not chute.isalpha():
            print("Resposta inválida")
            continue

        if chute in letras_sugeridas:
            print(f"{chute} já foi adivinhado")
            continue

        letras_sugeridas.add(chute)

        if chute in resposta:
            for i in range(len(resposta)):
                if resposta[i] == chute:
                    dica[i] = chute
        else:
            chutes_errados += 1

        if "_" not in dica:
            mostrar_cara(chutes_errados)
            mostrar_resposta(resposta)
            print("VOCÊ VENCEU!")
            is_running = False
        elif chutes_errados >= len(arte_forca) - 1:
            mostrar_cara(chutes_errados)
            mostrar_resposta(resposta)
            print("VOCÊ PERDEU!")
            is_running = False



if __name__ == "__main__":
    main()