from cinto_utilidades import despedida
print("Adicionando minha idade ao arquivo da questao anterior.\n")
arquivo = open("exemplo.txt", "w")
arquivo.write("Idade\n")
arquivo.write("Eu: 14\n")
arquivo.close()
despedida()