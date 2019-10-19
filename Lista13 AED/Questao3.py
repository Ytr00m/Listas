from cinto_utilidades import despedida
print("Adicionando ao arquivo da primeira questao a idade de meu pai e mae.\n")
arquivo = open("exemplo.txt", "a+")
arquivo.write("Mae: 55\n")
arquivo.write("Pai: 65\n")
arquivo.close()
despedida()