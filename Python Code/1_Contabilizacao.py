## A biblioteca abaixo nos permite obter informações do SO e interagir
import os

## Primeiro verifico se o caminho é válido
caminho = "/home/kali/Documents/GitHub/Python_repository"
def contar_pasta(x):
    if os.path.isdir(x):
        print("Caminho Válido")
    else: 
        print("Caminho Inválido")
        return
## Listo os arquivos
    listar_arquivos = os.listdir(x)
    cont = int()
    for c in listar_arquivos:
        if '.py' in c:
            cont = cont + 1
## Contabilizo os arquivos
    print(f"Qº de Arquivos: {cont+1}")
contar_pasta(caminho)