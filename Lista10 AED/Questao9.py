from cinto_utilidades import despedida
def fatorial(x):
    n = x - 1
    fat = x
    for i in range(1, x):
        fat *= n
        n -= 1
    return fat
def main():
    print("Fatorial de um numero\n")
    x = int(input("Numero: "))
    print(fatorial(x))
    despedida()
main()