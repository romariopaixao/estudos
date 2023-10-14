class Animal:
    def emitirSom(self):
        pass

class Cachorro(Animal):
    def emitirSom(self):
        print('MIAU! MIAU!')

class Pato(Animal):
    def emitirSom(self):
        print("Quack! Quack!")

class Veiculo:
    def __init__(self, cor, marca, modelo, velocidadeAtual):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.velocidadeAtual = velocidadeAtual

    def Acelerar(self):
        pass

    def exibir(self):
        print(f'Cor: {self.cor}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Velocidade atual: {self.velocidadeAtual}')

class Carro(Veiculo):
    def __init__(self, cor, marca, modelo, velocidadeAtual):
        super().__init__(cor, marca, modelo, velocidadeAtual)

    def Acelerar(self):
        self.velocidadeAtual += 25


class Moto(Veiculo):
    def __init__(self, cor, marca, modelo, velocidadeAtual):
        super().__init__(cor, marca, modelo, velocidadeAtual)

    def Acelerar(self):
        self.velocidadeAtual += 35


veiculo = Veiculo('vermelho', 'Volksvagem', 'gol', 10)
veiculo.Acelerar()
veiculo.exibir()

carro = Carro('preto', 'volksvagem', 'corsa', 10)
carro.Acelerar()
carro.exibir()

moto = Moto('branca', 'honda', 'bros', 10)
moto.Acelerar()
moto.exibir()

class FormaGeometrica:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcularArea(self):
        pass

class Triangulo(FormaGeometrica):
    def __init__(self, altura, base):
        super().__init__(altura, base)

    def calcularArea(self):
        return print(f'Area: {self.base * self.altura / 2}')

class Circulo(FormaGeometrica):
    def __init__(self, altura, base, raio):
        super().__init__(altura, base)
        self.raio = raio


    def calcularArea(self):
        return print(f'Area: {3.1415 * self.raio ** 2}')


class ConversorMoeda:
    def converter(self, valor):
        pass

class ConversorDolar(ConversorMoeda):
    def converter(self, valor):
        conversao = valor * 5.08
        print(f'O valor convertido ficou:{conversao}')

class ConversorEuro(ConversorMoeda):
    def converter(self, valor):
        conversao = valor * 5.34
        print(f'O valor convertido ficou:{conversao}')
