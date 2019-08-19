from cinto_utilidades import despedida
def peso_ideal(peso, altura):
    return peso / (altura ** 2)
def main():
    print("Peso ideal\n")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    print(peso_ideal(peso, altura))
    despedida()
main()
