import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
chave = chars.copy()

random.shuffle(chave)

print(f"chars: {chars}")
print(f"chave: {chave}")

#encrypt
texto =  input("Digite uma mensagem para encriptar: ")
cifra = ""

for letra in texto:
    index = chars.index(letra)
    cifra += chave[index]

print(f"Mensagem original: {texto}")
print(f"Mensagem encriptada: {cifra}")