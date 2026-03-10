# for para mostrar números
for i in range(1, 11):
    print(i, "Im freezing outside")

# criando uma lista com o mesmo número repetido
num = int(input("Digite um numero: "))
numeros = [num] * 10
print(numeros)

# preenchendo um vetor com valores digitados
valores = [0] * 6

for cont in range(0, len(valores)):
    valores[cont] = int(input("Informe o valor: "))

# mostrando os valores
for cont in range(0, len(valores)):
    print("Valor:", valores[cont])

# métodos (funções)
def fulano(a, b):
    mult = a * b
    print(mult)

# função para ler inteiro
def lerInt():
    x = int(input("Informe: "))
    return x

# usando as funções
a = lerInt()
b = lerInt()
fulano(a, b)
