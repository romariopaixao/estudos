# Como criar uma classe
class Aluno:
    # caracteristicas => atributos
    # comportamento/ações => métodos/funções

    #método construtor
    def __init__(self, mat, nome, curso):
        self.matricula = mat
        self.nome = nome
        self.curso = curso
        self.qtd_faltas = 0

    def aplicarFalta(self, qtd):
        self.qtd_faltas += qtd
        print(f"Falta atribuida com sucesso!")
        print(f"Faltas total: {self.qtd_faltas}")


    def exibirInformacoes(self):
        print("----------- INFORMAÇÕES DO ALUNO -----------")
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Curso: {self.curso}')
        print("----------- INFORMAÇÕES DO ALUNO -----------\n")

aluno1 = Aluno(1, "Romário Paixão", "Python")
aluno2 = Aluno(2, "Marina Rodrigues", "Java")

aluno1.exibirInformacoes()
aluno2.exibirInformacoes()
# Como acessa o atributo de um objeto
aluno1.aplicarFalta(3)
aluno1.aplicarFalta(5)
aluno2.aplicarFalta(10)

class Carro:
    def __init__(self, marca, modelo, cor, velocidade_max):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidadeAtual = 0
        self.velocidade_max = velocidade_max

    def acelerar(self, qtd):

        if self.velocidadeAtual + qtd <= self.velocidade_max:
            self.velocidadeAtual += qtd
            print("Velocidade adicionada com sucesso!")
            print(f"A velocidade atual do veiculo é {self.velocidadeAtual}")
        else:
            print("Valor inválido!")




    def desacelerar(self, qtd):
        self.velocidadeAtual -= qtd
        print(f"Velocidade dimuindo em ... {qtd}")
        print(f"Velocidade atual e {self.velocidadeAtual}")

carro1 = Carro("honda", "civic", "vermelha", 180)
carro2 = Carro("chevrolete", "civic", "preta", 180)

print(f"""
    Marca : {carro1.marca}
    modelo: {carro1.modelo}
    cor: {carro1.cor}
    """)
print(f"""
    Marca : {carro2.marca}
    modelo: {carro2.modelo}
    cor: {carro2.cor}
""")

carro1.acelerar(10)
carro1.acelerar(30)
print(carro1.velocidadeAtual)

carro1.desacelerar(15)
print(carro1.velocidadeAtual)

carro1.acelerar(200)

