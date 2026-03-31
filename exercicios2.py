class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
  
    def __init__(self, numero, cliente_objeto, saldo_inicial=0):
        self.numero = numero
        self.titular = cliente_objeto
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado para {self.titular.nome}!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado por {self.titular.nome}!")
            return True
        else:
            print(f"Saldo insuficiente para {self.titular.nome}!")
            return False

    def transferir(self, valor, conta_destino):
      
        if self.sacar(valor): 
            conta_destino.saldo += valor
            print(f"Transferência de {self.titular.nome} para {conta_destino.titular.nome} concluída!")




lucas_obj = Cliente("Lucas Henrique Silva", "123.456.789-00")
heloisa_obj = Cliente("Heloisa Gomes", "987.654.321-11")


conta1 = ContaBancaria(1, lucas_obj, 1000.00)
conta2 = ContaBancaria(2, heloisa_obj, 500.00)


print(f"Saldo Inicial - Lucas: R$ {conta1.saldo:.2f}")
print(f"Saldo Inicial - Heloisa: R$ {conta2.saldo:.2f}\n")

conta1.depositar(200.00)
conta2.sacar(300.00)
conta1.transferir(400.00, conta2)
conta2.sacar(1000.00)

print(f"\nSaldo Final - Lucas: R$ {conta1.saldo:.2f}")
print(f"Saldo Final - Heloisa: R$ {conta2.saldo:.2f}")