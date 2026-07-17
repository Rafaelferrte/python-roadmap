dia = input("Digite o dia:")

def dia_da_semana(dia):
    match dia:
        case 1:
            return "Hoje é Domingo!"
        case 2:
            return "Hoje é Segunda-Feira!"
        case 3:
            return "Hoje é Terça-Feira!"
        case 4:
            return "Hoje é Quarta-Feira!"
        case 5:
            return "Hoje é Quinta-Feira!"
        case 6:
            return "Hoje é Sexta-Feira!"
        case 7:
            return "Hoje é Sábado!"
        case _:
            return "Não é um dia válido"
    
print(dia_da_semana(1))

def e_final_de_semana(dia):
    match dia:
        case "Sábado" | "Domingo":
            return True
        case "Segunda-feira" | "Terça-feira" | "Quarta-feira" | "Quinta-feira" | "Sexta-feira":
            return False
        case _:
            False


print(e_final_de_semana(dia))