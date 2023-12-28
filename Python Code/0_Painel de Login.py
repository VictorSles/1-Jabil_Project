## A biblioteca que me permite criar esse arquivo é:
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
import tkinter as tk
import datetime
import pytz
import smtplib 
import os
## A biblioteca que me permite criar esse arquivo é:
caminho = "/home/kali/Documents/GitHub/1-Jabil_Project/Python Code/Pasta teste"
# 
#  Validação
#
if os.path.isdir(caminho):
    print("Valido")
else:
    print("Inválido")
    
## SOLVED
    
# Listagem + CONT_one
listagem = os.listdir(caminho)
cont = int()
for c in listagem:
    if ".txt" in c:
        cont = cont + 1

# CONTADOR



 ## SOLVED
 
# FUNÇÕES DE USO
def dataHora():
    data1 = pytz.timezone('America/Manaus')
    data_final = datetime.datetime.now(data1)
    return data_final.strftime("%d/%M/%Y %H:%M:%S")

def sobrescricao(x): ## CONT
    caminho_DB = "Python Code/ArquivoDB"
    listagem_DB = os.listdir(caminho_DB)
    try:
        for caminho in listagem_DB:
            caminho_final = f"{caminho_DB}/{caminho}"
            with open (caminho_final, "a") as arquivo_DB:
                arquivo_DB.write(f"\n{x}")
    except Exception as e:
        print(f"Erro >>> {e}")
dataHoraVar = dataHora() 

## SOLVED

# Condicional

def condicional(x):
    global caminho
    global listagem
    if x >= 10:
        for arquivo3 in listagem:
            lista_para_exclusao_3 = os.path.join(caminho, arquivo3)
            try:
                for i3 in lista_para_exclusao_3:
                    if os.path.isfile(lista_para_exclusao_3):
                        os.remove(lista_para_exclusao_3)
                        print(f"Arquivo Nº {arquivo3} excluido com sucesso!")
            except Exception as c:
                print(f"Error >>> {c}")
    elif x >= 20:
        for arquivo2 in listagem:
            lista_para_exclusao_2 = os.path.join(caminho, arquivo2)
            try:
                for i2 in lista_para_exclusao_2:
                    if os.path.isfile(lista_para_exclusao_2):
                        os.remove(lista_para_exclusao_2)
                        print(f"Arquivo Nº {arquivo2} excluido com sucesso!")
            except Exception as b:
                print(f"Error >>> {b}")
    elif x >= 30:
        for arquivo in listagem:
            lista_para_exclusao = os.path.join(caminho, arquivo)
            try:
                for i in lista_para_exclusao:
                    if os.path.isfile(lista_para_exclusao):
                        os.remove(lista_para_exclusao)
                        print(f"Arquivo Nº {arquivo} excluído com sucesso!")
            except Exception as a:
                    print(f"Error >>> {a}")
    return x
var1 = condicional(cont)
sobrescricao(var1)
### SOLVED

# E-mail
#def envio_email():
#    smtp_server = "smtp.gmail.com"
#    port = 587
#    email_sender = "israelvictords@gmail.com"
#    passW = "gsaa qlhd pjbi ljta"
#    email_receiver = "israelvic15@gmail.com"
#    mensagem = MIMEMultipart()
#    mensagem["From"] = email_sender
#    mensagem["To"] = email_receiver
#    mensagem["Subject"] = "TESTANDO A MINHA NOVA VERSÃO DO SOFTWARE"
#    body = "MAIS UM TESTE BEM SUCEDIDO!"
#    mensagem_2 = MIMEText(body, 'plain')
#    mensagem.attach(mensagem_2)
#    server = smtplib.SMTP("smtp.gmail.com: 587")
#    server.connect(smtp_server, port)
#    server.ehlo
#    server.starttls
#    server.ehlo
#    server.login(email_sender, passW)
#    texto = mensagem.as_string()
#    server.sendmail(email_sender, email_receiver, texto)
#    server.quit()
#envio_email()
##           
##  Painel de Login
##
#def verificar_credenciais():
#    usuario = entry_usuario.get()
#    senha = entry_senha.get()
#    if usuario == "123" and senha == "123":
#        messagebox.showinfo("OK", "Autenticação válida")
#        root.destroy()
#        root_login_2 = tk.Tk()
#        root_login_2.title("Informações de Contagem")
#        label_login_2 = tk.Label(root_login_2, text=f"Nº de arquivos: {cont}")
#        label_login_2.pack()
#        label_login_22 = tk.Label(root_login_2, text=f"{cont}")
#        label_login_22.pack()
#    else:
#        messagebox.showerror("NOK", "Autenticação Inválida")
### CRIAÇÃO DA INTERFACE SIMPLES
#root = tk.Tk()    ## Tk representa a JANELA PRINCIPAL
#root.title("Login")
#
### Criar campos de entrada para usuário e senha
#label_usuario = tk.Label(root, text="Usuário: ") ## Label serve para adicionar textos ou imagens dentro da interface
#label_usuario.pack() ## É um METODO de organização para posicionar os widgets dentro de um conteiner (aba de login no meu caso)
#entry_usuario = tk.Entry(root) ## Serve para adicionar a caixa que ira captar as informações do usuário
#entry_usuario.pack()
#
### O mesmo processo com a senha
#label_senha = tk.Label(root, text="Senha: ")
#label_senha.pack()
#entry_senha = tk.Entry(root, show="*")
#entry_senha.pack()
#
### Botao
#botao = tk.Button(root, text="Login", command=verificar_credenciais)
#botao.pack()
### O comando abaixo serve para iniciar a interface gráfica
#root.mainloop()