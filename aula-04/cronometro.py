import time

meu_tempo = int(input("Digite o tempo em segundos: "))

for x in range(0, meu_tempo):
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)



print("TEMPO ESGOTADO!")
