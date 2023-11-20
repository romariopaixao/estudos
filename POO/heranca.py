class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def exibirInformacoes(self):
        print("-------------------- DADOS DO FUNCIONÁRIO --------------------------")
        print(f'Matricula: {self.matricula}')
        print(f'Nome:{self.nome}')
        print(f'Salário: {self.salario}')


class Professor(Funcionario):
    def __init__(self, matricula, nome, salario, turma):
        # chamando o construtor de funcionario
        super().__init__(matricula, nome, salario)
        self.turma = turma

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Turma: {self.turma}")


class Monitor(Funcionario):
    # carga horaria
    def __init__(self, matricula, nome, salario, carga_horaria):
        super().__init__(matricula, nome, salario)
        self.carga_horaria = carga_horaria

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Carga horária: {self.carga_horaria}')


class Coordenador(Funcionario):
    # area
    def __init__(self, matricula, nome, salario, area):
        super().__init__(matricula, nome, salario)
        self.area = area

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Area: {self.area}")


class Veiculo():
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def exibirInformacoes(self):
        print("---------- INFORMAÇÕES ----------")
        print(f'Marca: {self.marca}')
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, rodas):
        super().__init__(marca, modelo, cor)
        self.rodas = rodas

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Numero de rodas: {self.rodas}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, cilindradas):
        super().__init__(marca, modelo, cor)
        self.cilindradas = cilindradas

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Cilindradas: {self.cilindradas}")

c1 = Carro("volkvagem", "modelo", "preta", 150)
c1.exibirInformacoes()

m1 = Moto("honda", "bross", "vermelha", 2)
m1.exibirInformacoes()