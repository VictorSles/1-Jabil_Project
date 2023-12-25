## VAMOS CRIAR VARIOS ARQUIVOS PORÉM SEM DEFINIR O CAMIMNHO

quant_arquivos = 11
def criarArquivos(x):
    for i in range(1, x+1):
        numeracao = f"Arquvivo Nº: {i}.txt"
        with open(numeracao, "w") as arquivo:   # WITH OPEN, é usado para manipular arquivos de forma segura garantindo seu fechamento corretamente ------ "w" é um parametro de siglas de comando usada pra manipular arquivos, outros exemplos são:
            # "r" - Read
            # "a" - Append __ abre o arquivo para adicionar algo ao final
            # "r+"- Read + Write
            # "w" - write
            
            ## No "as arquivo", estou associando o comando detalhado anteriormente a uma variável que funcionára como objeto de manipulação, nesse caso "arquivo"
            arquivo.write(f"{i}")   # Entre () é o conteúdo a ser escrito
            print(f"{numeracao} criado com sucesso!")
criarArquivos(quant_arquivos)