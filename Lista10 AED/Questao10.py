from cinto_utilidades import despedida
def potencia(base, expoente):
    n = 1
    for i in range(0, expoente):
        n *= base
    return n
def main():
    print("Poteciação\n")
    base = int(input("Base: "))
    expoente = int(input("Expoente: "))
    print(potencia(base, expoente))
    despedida()
main()
