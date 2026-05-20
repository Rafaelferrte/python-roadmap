def feliz_aniversario(nome):
    for i in range(3):
        print(f"Feliz Aniversário {nome}!!")

feliz_aniversario("Amigo")


def exibir_fatura(usuario, quantia, data_vencimento):
    print(f"Olá, {usuario}")
    print(f"Sua conta de R${quantia:.2f} vence: {data_vencimento}")

exibir_fatura("Rafael",76.88, "08/01")