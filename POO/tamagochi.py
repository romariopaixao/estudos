class Tamagochi:
    def __init__(self, nome, fome, energia):
        self.nome = nome
        self.fome = fome
        self.energia = energia

    def comer(self):

        if self.fome + 10 <= 100:
            self.fome += 10
            print(f"Comendo...Fome atual: {self.fome}")
        else:
            self.fome = 100
            print(f"{self.nome} está satisfeito. Fome atual: {self.fome}")

    def dormir(self):
        if self.energia + 15 <= 100:
            self.energia += 15
            print("Dormindo...")
            print(f"{self.nome} dormiu. Energia atual: {self.energia}")
        else:
            self.energia = 100
            print(f"{self.nome} esté energizado. Energia atual: {self.energia}")

    def passarTempo(self):
        self.fome -= 20
        self.energia -= 15
        print("Tempo passando..")
        print(f"Fome: {self.fome}. Energia: {self.energia}")

    def status(self):
        print(f'''
        --- Status Tamagochi ---
        Nome: {self.nome}
        Fome: {self.fome}
        Energia: {self.energia}
        ''')


bicho = Tamagochi("Sofia", 80, 80)
bicho.comer()
bicho.comer()
bicho.comer()
bicho.dormir()
bicho.dormir()
bicho.dormir()
bicho.passarTempo()
bicho.passarTempo()
bicho.status()