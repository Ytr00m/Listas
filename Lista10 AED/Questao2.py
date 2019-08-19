from cinto_utilidades import despedida
def soma(x, y):
    return x + y
def main():
    print("Soma de dois valores reais:\n")
    x = int(input("Numero 1: "))
    y = int(input("Numero 2: "))
    print(soma(x, y))
    despedida()
main()