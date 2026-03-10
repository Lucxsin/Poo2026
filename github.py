import os
print("Configurando email...")
comandoemail="git config user.email \"lucashenriquesilva0809@gmail.com\""
os.system(comandoemail)
print("adicionando modificações")
comando1="git add *"
os.system(comando1)

mensagem=input("Mensagem do commit: ")

while(len(mensagem)< 5):
    print("Mensagem muito pequena, detalhe mais...")
    mensagem=input("Mensagem do commit: ")
print("Adicionando mensagem")
comando2=f"git commit -m {mensagem}"
os.system(comando1)
print("Enviando ao github")
comando3="git push"
os.system(comando3)
print(comandoemail,comando1,comando2,comando3)
