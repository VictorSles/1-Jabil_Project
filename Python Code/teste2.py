# CONTATOR DE LINHAS 
import os
caminho = "Python Code/ArquivoDB"
caminho_2 = "Python Code/ArquivoDB_soma"
caminho_3 = "Python Code/exemplo"
listagem_1 = os.listdir(caminho)
listagem_2 = os.listdir(caminho_2)
listagem_3 = os.listdir(caminho_3)
for item1 in caminho:
    juncao = os.path.join(caminho, item1)
for item2 in caminho_2:
    juncao2 = os.path.join(caminho_2, item2)
for item3 in caminho_3:
    juncao3 = os.path.join(caminho_3, item3)
def funcao(x):
    try:
        with open(x, "r") as arquivo_ex:
            var = arquivo_ex.readline()
            var2 = len(var)
            print(var2)
    except Exception as e:
        print(f"Error >>> {e}")
contagem_atual = funcao(juncao)
def funcao2(y):
    global contagem_atual
    global 
    try:
        with open(y, "w") as arquivoDB:
            arquivoDB.write(str(contagem_atual))
        with open(contagem_atual, "r") as arquivo_leitura:
            for _ in range(contagem_atual):
                next(arquivo_leitura)
            with open(, "w") as 
            
            
            
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