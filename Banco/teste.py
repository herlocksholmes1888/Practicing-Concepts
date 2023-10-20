from clientes import Cliente
from banco import Banco
from contas import Conta, ContaEspecial

joao = Cliente("João Medeiros de Souza Neto", "(13) 98887-7755")
maria = Cliente("Maria Helena Hasaam Albuquerque", "(13) 9558-7473")
jose = Cliente("José Gilberto Amado Meireles", "(13) 92234-4491")

conta1 = ContaEspecial([maria, joao], 1, 100, 500)
conta2 = Conta([jose], 2)

conta1.saque(300)
conta1.extrato()

santander = Banco("Santander")
santander.abre_contas(conta1)
santander.abre_contas(conta2)
# santander.lista_contas()
