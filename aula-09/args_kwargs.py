def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5))

def mostrar_nome(*args):
    nome = ""
    for arg in args:
        nome += arg + " "
    return nome

print(mostrar_nome("Rafael","Ferrete"))


def exibir_endereco(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

exibir_endereco(rua="12,St. Fake",
                cidade="Registro",
                estado="SP",
                cep="11900-000")