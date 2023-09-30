class Conta:
    def __init__(self, num_conta, nome_cliente, saldo, rendimento):
        self.num_conta = num_conta
        self.nome_cliente = nome_cliente
        self.saldo = saldo
        self.taxa_rendimento = rendimento

    def depositar(self, valor):
        self.saldo += valor
        print(f"Transferencia concluida. Novo saldo é {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque concluido. Saldo atual {self.saldo}")
        else:
            print("Saldo insuficiente!")

    def aplicarRendimento(self):
        self.saldo += self.saldo * self.taxa_rendimento / 100
        print(f"Rendimento aplicado. Saldo atual: {self.saldo}")

    def exibirDados(self):
        print(f"""
                Numero da conta: {self.num_conta}
                Cliente: {self.nome_cliente}
                Saldo: {self.saldo}    
        """)

conta1 = Conta(1, "roma", 100.0, 10)


conta1.exibirDados()

conta1.depositar(150)
conta1.exibirDados()

conta1.sacar(100)
conta1.exibirDados()
conta1.sacar(1000)

conta1.aplicarRendimento()