from cinto_utilidades import despedida
print("Coisas escritas no arquivo.\n")
arq = open("exemplo.txt", "r")
print(arq.read())
arq.close()
despedida()
