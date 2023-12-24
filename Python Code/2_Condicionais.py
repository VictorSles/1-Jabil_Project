## TESTE SOFTWARE ContDoc_Jabil
import time
lista = list(range(1,50003))
cont = int()
for i in lista:
    cont = cont + 1
if cont >= 1000:
    lista = 0
if cont >= 50000:
    print(cont, "!!!")
    print("*"*100)
    time.sleep(2)
    var1 = str(input("1) E-mail: "))
    var2 = str(input("2) E-mail: "))
    var3 = str(input("3) E-mail: "))
    print(f"""
          Enviando email para:
          
          {var1}
          {var2}
          {var3}
          
          Aguarde...
          """)
    time.sleep(3)
    print("E-mails enviados com sucesso!")
else:
    print("Tudo dentro do límite.")
print(cont)