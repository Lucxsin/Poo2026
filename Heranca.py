class Animal:
    def __init__(self, nome, especie, patas):
        self.nome = nome
        self.especie = especie
        self.patas = patas

    def respirar(self):
        print(f"{self.nome} está respirando...")

    def rugir(self):
        print("O animal vai rugir!")


class Cachorro(Animal):
    def abanar_rabo(self):
        print("Abanando o rabo...")

    def rugir(self):
        print("AU AU")


class Gato(Animal):
    def ronronar(self):
        print("Ronronando...")

    def rugir(self):
        print("Miau")