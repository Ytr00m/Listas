from cinto_utilidades import despedida
def primaridade(x):
    divisor, divisores = 1, 0
    while divisor <= x:
        div = x % divisor
        if div == 0:
            divisores += 1
        divisor += 1
    if divisores == 2:
        return 'eh primo'
    else:
        return 'nao eh primo'
def main():
    print("Indentificando se um numero é primo ou nao\n")
    x = int(input("Numero: "))
    print(primaridade(x))
    despedida()
main()