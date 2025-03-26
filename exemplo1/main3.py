arquivo = open("texto.txt", "r")
linha = arquivo.readline()
while linha != "":
    print(linha)
    linha = arquivo.readline()
arquivo.close()
