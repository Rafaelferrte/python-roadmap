def ola(saudacao, titulo, primeiro, ultimo):
    print(f"{saudacao} {titulo}{primeiro} {ultimo}")

ola("Olá",titulo="Mr.",primeiro="Bobesponja",ultimo="calçaquadrada")

for x in range(1,11):
    print(x, end=" ")

def pegar_numero(pais, area, primeiro, ultimo):
    return f"{pais}-{area}-{primeiro}-{ultimo}"

print()
num_cel = pegar_numero(pais=55,area=13, primeiro=30343, ultimo=4345)
print(num_cel)