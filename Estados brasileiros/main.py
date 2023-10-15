from estados import Estados 
from cidades import Cidades

mg = Estados("Minas Gerais", "MG")
mg.adiciona_cidade(Cidades("Belo Horizonte", 272200))
mg.adiciona_cidade(Cidades("Ouro Preto", 74558))

rs = Estados("Rio Grande do Sul", "RS")
rs.adiciona_cidade(Cidades("Porto Alegre", 133257))
rs.adiciona_cidade(Cidades("Pelotas", 343132))

sp = Estados("São Paulo", "SP")
sp.adiciona_cidade(Cidades("São Paulo", 1233000))
sp.adiciona_cidade(Cidades("Campos do Jordão", 52405))

print(mg.lista_cidade())
print(rs.lista_cidade())
print(sp.lista_cidade())

print("---")

print(mg.soma_populacao_estado())
print(rs.soma_populacao_estado())
print(sp.soma_populacao_estado())
