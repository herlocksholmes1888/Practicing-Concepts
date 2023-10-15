class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla 
        self.cidades = []

    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)

    def soma_populacao_cidade(self):
        return sum([c.populacao for c in self.cidades]) 

    def lista_cidades(self):
        for cidade in self.cidades:
            print(cidade.nome) # print(cidade) retorna o local em que o objeto está na memória