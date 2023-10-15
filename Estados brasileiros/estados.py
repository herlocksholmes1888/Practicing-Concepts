class Estados:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = [] 

    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)

    def lista_cidade(self):
        for cidade in self.cidades:
            print(cidade.nome)

    def soma_populacao_estado(self):
        return sum(cidade.populacao for cidade in self.cidades)
    