class Aluno:
    # Método/Funções construtor
    def __init__(self, matricula, nome, curso, nota):
        # Definindo os atributos do aluno
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.nota = nota
        self.qtd_faltas = 0
        # print(f'aluno criado: {self.nome}')
    def exibirDados(self):
        print(f''''
                matricula: {self.matricula}
                nome: {self.nome}
                curso: {self.curso}
                nota: {self.nota}
                Quantida de faltas: {self.qtd_faltas}
            ''')
    def atribuirFalta(self, qtd=0):
        if qtd > 0:
            self.qtd_faltas += qtd
        else:
            self.qtd_faltas += 1
        print(f"Faltas atribuidas com sucesso! Faltas: {self.qtd_faltas}")


#Como criar um objeto
aluno1 = Aluno(1, "romario", "Django", 8.0)
aluno2 = Aluno(2, "Marina", "pyhton", 10)

aluno1.exibirDados()
print('----')
aluno2.exibirDados()
aluno1.atribuirFalta()
aluno1.atribuirFalta()
aluno1.atribuirFalta(7)
aluno1.exibirDados()
# Como acesar as propriedades de um objeto
print(f"Nota do aluno1: {aluno1.nota}")
aluno1.nota = 10
print(f"Nova nota do aluno1: {aluno1.nota}")

class Conta:
    def __init__(self, numero_da_conta, nome_do_cliente, saldo):
        self.numero_da_conta = numero_da_conta
        self.nome_do_cliente = nome_do_cliente
        self.saldo = saldo
    def exibirDados(self):
        print(f'''
        Numero da conta: {self.numero_da_conta}
        Nome do cliente: {self.nome_do_cliente}
        Saldo: {self.saldo}
        ''')



conta1 = Conta(1, "Romário", 1000)
conta2 = Conta(2, "Kessia", 15000)

conta1.exibirDados()
conta2.exibirDados()