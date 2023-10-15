from estados_tentando import Estado
from cidades_tentando import Cidade

mg = Estado("Minas Gerais", "MG")
mg.adiciona_cidade(Cidade("Belo Horizonte", 272200))
mg.adiciona_cidade(Cidade("Ouro Preto", 74558))

rs = Estado("Rio Grande do Sul", "RS")
rs.adiciona_cidade(Cidade("Porto Alegre", 133257))
rs.adiciona_cidade(Cidade("Pelotas", 343132))

sp = Estado("São Paulo", "SP")
sp.adiciona_cidade(Cidade("São Paulo", 1233000))
sp.adiciona_cidade(Cidade("Campos do Jordão", 52405))

print(mg.lista_cidades())
print(rs.lista_cidades())
print(sp.lista_cidades())

print("---")

print(mg.soma_populacao_cidade())
print(rs.soma_populacao_cidade())
print(sp.soma_populacao_cidade())