class Conta:
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Deposito realizado com sucesso!')
            print(f'Seu saldo: R${self.saldo}')
        else:
            print('Valor invalido')

class ContaCorrente(Conta):
    def __init__(self, numero, nome, saldo, limite):
        self.limite = limite
        super().__init__(numero, nome, saldo)

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print('Saque realizado com sucesso')
            print(f'Saldo atual: R$ {self.saldo}')
        else:
            print('Saldo insuficiente!')

class ContaPoupanca(Conta):
    def __init__(self, numero, nome, saldo, taxa_rendimento):
        super().__init__(numero, nome, saldo)
        self.taxa_rendimento = taxa_rendimento

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
            print(f'Saldo atual: R$ {self.saldo}')
        else:
            print(f'Saldo insuficiente!')

    def calcularRendimento(self):
        self.saldo += self.saldo * self.taxa_rendimento
        print('Rendimentos calculados')
        print(f'Saldo atual: R$ {self.saldo}')


contaCorrente = ContaCorrente(1, "Roma", 1000.0, 250)
contaCorrente.depositar(100)
contaCorrente.sacar(1350)

contaPoup = ContaPoupanca(2, 'Ellen', 1000, 0.2)
contaPoup.depositar(1000)
contaPoup.calcularRendimento()
contaPoup.sacar(2000)