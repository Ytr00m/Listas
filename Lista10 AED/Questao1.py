from cinto_utilidades import despedida
def maior(x, y):
    if x > y:
        return x
    else:
        return y
def main():
    print("Maior entre dois numeros reais:\n")
    x = int(input("Numero 1: "))
    y = int(input("Numero 2: "))
    print(maior(x, y))
    despedida()
main()
