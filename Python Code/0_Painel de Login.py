## A biblioteca que me permite criar esse arquivo é:
import os
import tkinter as tk
from tkinter import messagebox

caminho = "/home/kali/Documents/GitHub/Python_repository"
## Validação
if os.path.isdir(caminho):
    print("Valido")
else:
    print("Inválido")
## Listagem
listagem = os.listdir(caminho)
cont = int()
for c in listagem:
    if ".py" in c:
        cont = cont + 1
cont += 1
if cont >= 1000:
    for arquivo in caminho:
        lista_para_exclusao = os.path.join(caminho, arquivo)
    try:
        if os.path.isfile(lista_para_exclusao):
            os.remove(lista_para_exclusao)
            print("Arquivo excluidos com sucesso")
    except Exception as e:
        print(f"Error: {e}")

def verificar_credenciais():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == "123" and senha == "123":
        messagebox.showinfo("OK", "Autenticação válida")
        root.destroy()
        root_login_2 = tk.Tk()
        root_login_2.title("Informações")
        label_login_2 = tk.Label(root_login_2, text="ABC")
        label_login_2.pack()
        label_login_22 = tk.Label(root_login_2, text="123")
        label_login_22.pack()
    else:
        messagebox.showerror("NOK", "Autenticação Inválida")
## CRIAÇÃO DA INTERFACE SIMPLES
root = tk.Tk()    ## Tk representa a JANELA PRINCIPAL
root.title("Login")

## Criar campos de entrada para usuário e senha
label_usuario = tk.Label(root, text="Usuário: ") ## Label serve para adicionar textos ou imagens dentro da interface
label_usuario.pack() ## É um METODO de organização para posicionar os widgets dentro de um conteiner (aba de login no meu caso)
entry_usuario = tk.Entry(root) ## Serve para adicionar caixar que irao captar as informações do usuário
entry_usuario.pack()

## O mesmo processo com a senha
label_senha = tk.Label(root, text="Senha: ")
label_senha.pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

## Botao
botao = tk.Button(root, text="Login", command=verificar_credenciais)
botao.pack()
label_erro = tk.Label(root, fg="red")
label_erro.pack()
## O comando abaixo serve para iniciar a interface gráfica
root.mainloop()