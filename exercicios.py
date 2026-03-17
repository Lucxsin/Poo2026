



# # def verifica_par(valor1):
# #     if valor1 % 2 == 0:
# #         return True
# #     else:
# #         return False

# # valor1 = int(input("Informe um valor: "))
# # result = verifica_par(valor1)

# # if result:
# #     print("é par")
# # else:
# #     print("ímpar")

# def calcDesconto(precos,desconto):
#     for i in range(0,len(precos)):
#         desconto=precos[i]*(p/100)
#         valor=precos[i]-descontoprecos[]
# while opcao != 4:
#     print("\n=== MENU ===")
#     print("1 - Cadastrar produto")
#     print("2 - Mostrar produtos e preços")
#     print("3 - Aplicar desconto")
#     print("4 - Sair")

#     opcao = int(input("Escolha uma opção: "))

#     if opcao == 1:
#         nome = input("Digite o nome do produto: ")
#         preco = float(input("Digite o preço: "))
        
     
        
#         print("Produto cadastrado com sucesso!")

#     elif opcao == 2:
#         print("\nLista de produtos:")
#         for i in range(len(produtos)):
#             print(f"{produtos[i]} - R$ {precos[i]:.2f}")

#     elif opcao == 3:
#         desconto = float(input("Digite o desconto (%): "))
        
#         for i in range(len(precos)):
#             precos[i] = precos[i] * (1 - desconto / 100)
        
#         print("Desconto aplicado!")

#     elif opcao == 4:
#         print("Saindo do programa...")

#     else:
#         print("Opção inválida!")


class Eleven:
    def __init__(self):
        self.nome = "Eleven"
        self.apelido = "El"
        self.poderes = "Telecinese"
        self.nivel_energia = 100
        self.fome_waffles = True

    def usar_poderes(self, objeto):
        if self.nivel_energia > 20:
            print(f"{self.nome} está usando telecinese para mover: {objeto}!")
            self.nivel_energia -= 30
            print("Sangue no nariz? Sim.")
        else:
            print(f"{self.nome} está sem energia. Precisa de Waffles!")

    def comer_waffle(self):
        print(f"{self.nome} está comendo Eggos.")
        self.nivel_energia += 50
        self.fome_waffles = False

# Criando a Eleven
el = Eleven()
el.usar_poderes("Van do Brenner")
el.comer_waffle()
import time

def eleven_simulation():
    energia = 100
    print("--- Eleven Iniciando ---")
    
    for i in range(3):
        print(f"\nEleven usando poderes... Energia: {energia}")
        energia -= 40
        time.sleep(1)
        
        if energia <= 20:
            print(">> Eleven: 'PRECISO DE WAFFLES!'")
            energia += 60
            print(">> Eleven comeu Waffles. Energia restaurada.")
            
    print("\nEleven está descansando.")

eleven_simulation()
# Simulação do código de segurança de ST2
def verificar_codigo(porta):
    if porta == "aberta":
        return "Demogorgon liberado!"
    else:
        return "Porta segura."

# A Eleven fechando o portal
def fechar_portal():
    print("Eleven concentrada...")
    return "Portal Fechado (Mundo Invertido)".upper()

print(fechar_portal())
