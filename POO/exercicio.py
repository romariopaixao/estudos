from time import sleep

"""1. Crie uma classe para representar um Elevador com os seguintes atributos
- andar atual (terreo = 0)
- quantidade de andares
- capacidade (qtd de pessoas que podem ter no elevador)
- qtd pessoas (dentro do elevador)
"""
"""2. Crie as seguintes funções pro elevador
subir() -> sobe um andar (não pode passar do ultimo andar)
descer() -> desce um andar (não pode passar do terreo)
entrar(qtd) -> não pode ultrapassar a capacidade
sair(qtd) -> não pode ficar com qtd pessoas negativa"""
class Elevador:
    def __init__(self, andar_atual, qtd_andares, capacidade, qtd_pessoa):
        self.andar_atual = andar_atual
        self.qtd_andares = qtd_andares
        self.capacidade = capacidade
        self.qtd_pessoa = qtd_pessoa
        self.nome_obj = self

    def subir(self, valor: int):
        if valor + self.andar_atual <= self.qtd_andares:
            self.andar_atual =+ valor
            print("Estamos subindo....")
            for andar in range(valor):
                print(f"Estamos no andar {andar} e subindo...")
                sleep(0.2)

        else:
            print(f"Você não pode subir mais do que {self.qtd_andares}")

    def descer(self, valor: int):
        if self.andar_atual - valor < 0:
            print("voce nao pode descer abaixo do andar 0")
        else:
            self.andar_atual -= valor
            print("estamos descendo.")

    def entrar(self, num_pessoas: int):
        if num_pessoas + self.qtd_pessoa < self.capacidade:
            self.qtd_pessoa += num_pessoas
            print(f"{num_pessoas} entraram no elevador")
        else:
            print(f"Esse numero de pessoas excer a capacidade maxima do elevador")

    def sair(self, num_pessoas: int):
        if self.qtd_pessoa - num_pessoas >= 0:
            self.qtd_pessoa -= num_pessoas
            print("saindo..")
            print(f'Quantidade de pessoas {self.qtd_pessoa}')
        else:
            print('Quantidade de pessoas saindo mais doq entrou ')


    def exibir_dados(self):
        print(f"""
            {"-"*20} INFORMAÇÕES ELEVADOR {"-"*20} 
            Andar atual:{self.andar_atual}
            Quantidade de andares: {self.qtd_andares}
            Capacidade de pessoas: {self.capacidade}
            Quantidade de pessoas: {self.qtd_pessoa}
            Nome do elevador: {self.nome_obj}
            {"-"*20} INFORMAÇÕES ELEVADOR {"-"*20} 
            """)



elevador1 = Elevador(0,15,10,5)
elevador1.subir(15)
elevador1.exibir_dados()

elevador1.descer(15)
elevador1.descer(14)
elevador1.entrar(5)
elevador1.sair(5)
elevador1.exibir_dados()