from cinto_utilidades import despedida
def paridade(x):
    if x % 2 == 0:
        return 'eh par'
    else:
        return 'nao eh par'
def main():
    print("Indentificando se um numero é par ou nao\n")
    x = int(input("Numero: "))
    print(paridade(x))
    despedida()
main()