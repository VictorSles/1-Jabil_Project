## Quero fazer com que a cada execução, um arquivo especifico seja lido e reescrito
import os
import datetime
from datetime import datetime       ## Parece estranho mas é necessário
import pytz
def funcao(x):
    var = x + 10
    return var
varDB = funcao(26)
caminho = "Python Code/Pasta teste"

## funcao dia e hora
def tempo():
    data1 = pytz.timezone('America/Manaus')
    data2 = datetime.now(data1)
    return data2.strftime("%d/%m/%Y %H:%M:%S")
varQualquer = tempo()
print(varQualquer)
if os.path.isdir(caminho):
    print("SIM É")
else:
    print("NÃO É")
listagem = os.listdir(caminho)
for x in listagem:
    y = f"{caminho}/{x}"
    cont = f"{varDB}"
    with open(y, "a") as alteracao:
        alteracao.write(f"[{varQualquer}] >>> Qº de arquivos criado: {cont}\n")
        
        
        
        
