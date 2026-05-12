import math

class Calculadora:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Soma
    def somar(self, a, b, c=0):
        return a + b + c

    # Subtração
    def subtrair(self, a, b, c=0):
        return a - b - c

    # Multiplicação
    def multiplicar(self, a, b, c=1):
        return a * b * c

    # Divisão
    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisão por zero!"
        return a / b


class CalculadoraCientifica(Calculadora):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.funcoes_cientificas = "Potência e Raiz Quadrada"

    def potencia(self, base, expoente):
        return base ** expoente

    def raiz_quadrada(self, numero):
        if numero < 0:
            return "Erro: número negativo!"
        return math.sqrt(numero)



print("=== CALCULADORA ===")

marca = input("Marca: ")
modelo = input("Modelo: ")
ano = int(input("Ano: "))

calc = Calculadora(marca, modelo, ano)

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("\nResultados:")
print("Soma:", calc.somar(a, b))
print("Subtração:", calc.subtrair(a, b))
print("Multiplicação:", calc.multiplicar(a, b))
print("Divisão:", calc.dividir(a, b))

print("\n=== CALCULADORA CIENTÍFICA ===")

calc_cient = CalculadoraCientifica("Casio", "FX-991", 2024)

valor = float(input("Digite um valor: "))

print("Valor ao cubo:", calc_cient.potencia(valor, 3))
print("Raiz quadrada:", calc_cient.raiz_quadrada(valor))

