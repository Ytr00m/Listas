from cinto_utilidades import despedida
def perimetro(x):
    return x * 4
def main():
    print("Perimetro de um quadrado\n")
    x = int(input("Lado: "))
    print(perimetro(x))
    despedida()
main()