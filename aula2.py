numero = int(input("Digite um numero: "))
if(numero > 100):
    print("A metade é", numero / 2)
else:
    print("O numero não vai rodar né burro")


num = int(input("Digite um num: "))
if(num % 2 == 0):
    print("Esse numero é par")
else:
    print("Não é par")


num1 = int(input("Digite um num: "))
num2 = int(input("Digite outro num: "))
sinal = str(input("Adicione um sinal operacional (+ - * /): "))

if(sinal == "+"):
    print("O resultado", num1 + num2)
elif(sinal == "-"):
    print("Resultado", num1 - num2)
elif(sinal == "*"):
    print("Resultado", num1 * num2)
elif(sinal == "/"):
    print("Resultado", num1 / num2)


nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: R$ "))

print("Olá", nome, ". Você tem", idade, "anos.")

if(salario <= 10000):
    print(f"Você ganha muito mal: R${salario:.2f}")
elif(salario > 10000 and salario < 20000):
    print(f"Você ganha bem R${salario:.2f}")
else:
    print(f"Você ganha muito bem!! R${salario:.2f}")


import random

valor1 = int(input("Informe um valor: "))
valor = random.randint(10, 15)

if(valor1 == valor):
    print("Você acertou")
else:
    print("Você errou")


from math import sqrt

valor = sqrt(16)
print(valor)


num = 0
while(num < 10 or num > 15):
    num = int(input("Digite um valor entre 10 e 15: "))

sorte = random.randint(10, 15)

if sorte == num:
    print("Você acertou!", sorte)
else:
    print("Você errou!", sorte)


sorte = random.randint(1, 10)
print("Valor é", sorte)

numero = int(input("Digite o valor que foi sorteado: "))

while(numero != sorte):
    print("Valor inválido")
    numero = int(input("Digite o valor que foi sorteado: "))

print("Você acertou")


for i in range(1, 11):
    print(i)


numeros = [0] * 10
print(numeros)
    
