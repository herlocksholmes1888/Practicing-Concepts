class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.clientes = clientes 
        self.numero = numero
        self.saldo = saldo 
        self.operacoes = []

    def extrato(self):
        print("CC Nº %s Saldo: %10.2f " % (self.numero, self.saldo))
        for o in self.operacoes:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n Saldo: %10.2f\n" % self.saldo)

    def resumo(self):
        print("CC Nº %s Saldo: %10.2f " % (self.numero, self.saldo))
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print("O valor que deseja sacar é inferior ao valor que se encontra em sua conta bancária.")
            return False
        
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite = 0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE: ", valor])
            return True
        else:
            return False
        
    def extrato(self):
        Conta.extrato(self)
        print("Limite atual: %10.2f" % self.limite)
