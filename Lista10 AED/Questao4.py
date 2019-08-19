from cinto_utilidades import despedida
def area_circulo(x):
    return 3.14 * (x ** 2)
def main():
    print("Calculo da area de um circulo\n")
    x = int(input("Raio: "))
    print(area_circulo(x))
    despedida()
main()