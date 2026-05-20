import time

def cont(fim,inicio=0):
    for x in range(inicio, fim+1):
        print(x)
        time.sleep(1)
    print("Acabou!!")

cont(10)











# Default arguments
def net_preco(lista_preco, desconto=0, taxa=0.05):
    return lista_preco * (1 - desconto) * (1 + taxa)

net_preco(500, 0.1, 0)