quant = 40
for arquivo in range(quant+1):
    conteudo = f"Texto Nº{arquivo}.txt"
    with open(conteudo, "w") as arquivo2:
        arquivo2.write(f"{arquivo}")
        print(f"Arquivo Nº{arquivo} criado com sucesso!")
print("Fim")
