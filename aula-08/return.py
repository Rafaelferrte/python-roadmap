z = 3

def adicao(x,y):
    z = x + y
    return z

def subtracao(x,y):
    z = x - y
    return z

def multiplicacao(x,y):
    z = x * y
    return z

def divisao(x,y):
    z = x / y
    return z

adicao(1,2)
subtracao(1,2)
multiplicacao(1,2)
divisao(1,2)


def criar_nome(primeiro, ultimo):
    primeiro = primeiro.capitalize()
    ultimo = ultimo.capitalize()
    return primeiro + " " + ultimo

nome_completo = criar_nome("Bob", "Esponja")
print(nome_completo)
