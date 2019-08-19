from cinto_utilidades import despedida
def maior_valor(lista):
    return max(lista)
def main():
    print("Maior valor em uma sequencia terminada por 0\n")
    x, lista = 1, []
    while x != 0:
        x = int(input("Numero: "))
        lista.append(x)
    lista.remove(0)
    print(maior_valor(lista))
    despedida()
main()
