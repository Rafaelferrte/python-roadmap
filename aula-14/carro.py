class Carro:
    def __init__(self, modelo, ano, cor, a_venda):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.a_venda = a_venda

    def dirigir(self):
        print(f"Você dirigiu o {self.modelo}")

    def pare(self):
        print(f"Você parou o {self.modelo}")
