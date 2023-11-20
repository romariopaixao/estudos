class Conta:
    def __init__(self, numero, nome, saldo):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def getNumero(self):
        return self.__numero

    def setNumero(self, valor):
        self.__numero = valor

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, valor):
        self.__saldo = valor

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome


conta1 = Conta(1, 'Luiz', 1000)


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
    def getIdade(self):
        return self.__idade
    def setIdade(self, valor):
        self.__idade = valor
    def getCpf(self):
        return self.__cpf
    def setCpf(self, valor):
        self.__cpf = valor


class Usuario:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    def getLogin(self):
        return self.__login

    def setLogin(self, nome):
        self.__login = nome

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        if len(senha) >= 6 and ('!' in senha or '@' in senha):
            self.__senha = senha
        else:
            print("Senha invalida tente outra senha")