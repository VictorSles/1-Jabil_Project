## As bibliotecas que me permitem criar esse script é:
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
import tkinter as tk
import datetime
import pytz
import smtplib 
import os
#####################################################
caminho = "Python Code/Pasta teste"
caminho_2 = "Python Code/ArquivoDB"
caminho_3 = "Python Code/ArquivoDB_soma"
if os.path.isdir(caminho):
    print("Valido")
else:
    print("Inválido")
listagem = os.listdir(caminho)
cont = int()
for c in listagem:
    if ".txt" in c:
        cont = cont + 1
listagem_2 = os.listdir(caminho_2)
listagem_3 = os.listdir(caminho_3)
def dataHora():
    data1 = pytz.timezone('America/Manaus')
    data_final = datetime.datetime.now(data1)
    return data_final.strftime("%d/%M/%Y %H:%M:%S")
def sobrescricao(x): ## CONT
    global listagem
    global caminho_2
    listagem_DB = os.listdir(caminho_2)
    try:
        for item in listagem_DB:
            caminho_final = os.path.join(caminho_2, item)
            with open (caminho_final, "a") as arquivo_DB:
                arquivo_DB.write(f"{x}")
        return x
    except Exception as e:
        print(f"Error >>> {e}")
def leitura_2(): ## LEITURA CONT
    global caminho_2
    global caminho_3
    global listagem_2
    global listagem_3
    for item in listagem_2:
        caminho_arquivo = os.path.join(caminho_2, item)
        with open(caminho_arquivo, "r") as arquivo_DB_read:
            linhas = [int(line.strip()) for line in arquivo_DB_read.readlines()]
            total = max(linhas)
            linhas_2 = len(linhas) - 1
            if linhas_2:
                for item_2 in listagem_3:
                    leitura_Arquivo_DB_soma = os.path.join(caminho_3, item_2)
                    with open(leitura_Arquivo_DB_soma, "r") as arquivo_DB_soma_read:
                        var_Arquivo_DB = arquivo_DB_soma_read.read()
                        var_Arquivo_DB = int(var_Arquivo_DB)
                        soma = var_Arquivo_DB + 1
                        return soma
def sobrescricao_2(x):
    global caminho_3
    listagem_3
    x = str(x)
    try:
        for item in listagem_3:
            juncao_caminho = os.path.join(caminho_3, item)
            with open(juncao_caminho, "w") as arquivoDB_soma_file:
                arquivoDB_soma_file.write(x)
        return x, "OK"
    except Exception as e:
        print(f"Error >>> {e}")
def espacamento():
    global caminho_2
    global listagem_2
    for item in listagem_2:
        caminho_arquivo = os.path.join(caminho_2, item)
        with open(caminho_arquivo, "a") as alteracao_arquivo_DB:
            alteracao_arquivo_DB.write(f"\n")
            print("Alteração realizada com sucesso!")
dataHoraVar = dataHora() 
def envio_email():
    smtp_server = "smtp.gmail.com"
    port = 587
    email_sender = "israelvictords@gmail.com"
    passW = "gsaa qlhd pjbi ljta"
    email_receiver = "israelvic15@gmail.com"
    mensagem = MIMEMultipart()
    mensagem["From"] = email_sender
    mensagem["To"] = email_receiver
    mensagem["Subject"] = "TESTANDO A MINHA NOVA VERSÃO DO SOFTWARE"
    body = "MAIS UM TESTE BEM SUCEDIDO!"
    mensagem_2 = MIMEText(body, 'plain')
    mensagem.attach(mensagem_2)
    server = smtplib.SMTP("smtp.gmail.com: 587")
    server.connect(smtp_server, port)
    server.ehlo
    server.starttls
    server.ehlo
    server.login(email_sender, passW)
    texto = mensagem.as_string()
    server.sendmail(email_sender, email_receiver, texto)
    server.quit()
def condicional(x, y):
    global caminho
    global caminho_2
    global listagem
    global listagem_2
    global envio_email
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
    if y >= 20:
        envio_email()
    return x
#
#
#
var_leitura_2 = leitura_2()
var_return_1 = condicional(cont, var_leitura_2)
var_return_3 = sobrescricao(var_return_1)
print(var_leitura_2, "mais um teste")
sobrescricao_2(var_leitura_2)
espacamento()
### SOLVED
# E-mail

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