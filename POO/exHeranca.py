class Conta:
    def __init__(self, num_conta, nome_cliente, saldo):
        self.num_conta = num_conta
        self.nome_cliente = nome_cliente
        self.saldo = saldo

    def exibirInformacao(self):
        print("---------- INFORMAÇÃO ----------")
        print(f"Numero conta: {self.num_conta}")
        print(f"Nome cliente: {self.nome_cliente}")
        print(f"Saldo: {self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, num_conta, nome_cliente, saldo, cheque_especial):
        super().__init__(num_conta, nome_cliente, saldo)
        self.cheque_especial = cheque_especial

    def exibirInformacao(self):
        super().exibirInformacao()
        print(f"Cheque especial: {self.cheque_especial}")

class ContaPoupanca(Conta):
    def __init__(self, num_conta, nome_cliente, saldo, tx_rendimento):
        super().__init__(num_conta, nome_cliente, saldo)
        self.tx_rendimento = tx_rendimento

    def exibirInformacao(self):
        super().exibirInformacao()
        print(f"Taxa de rendimento: {self.tx_rendimento}")


cc = ContaCorrente(1, "romario", 100, 50)
cc.exibirInformacao()

cp = ContaPoupanca(2, "jose", 200, 10)
cp.exibirInformacao()