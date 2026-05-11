# CALCULADORA IMC
peso = float(input("Digite o seu peso (Kg): "))
altura = float(input("Digite sua altura (cm): ")) / 100

imc = round(peso / (altura ** 2), 2)
print(f"\nIMC: {imc}")

if (imc<18.5):
    classificacao ="Abaixo do peso normal"
elif (imc<= 24.9):
    classificacao = "Peso normal"
elif (imc<=29.9):
    classficacao = "Excesso de peso"
elif (imc<=34.9):
    classificacao = "Obesidade classe I"
elif (imc<=39.9):
    classificacao = "Obesidade classe II"
else:
    classificacao = "Obesidade classe III"


print(classificacao)