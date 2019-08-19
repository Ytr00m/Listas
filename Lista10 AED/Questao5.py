from cinto_utilidades import despedida
def bissexto(x):
    ebi = True
    if x % 4 != 0:
        ebi = False
    elif x % 100 == 0:
        ebi = False
    elif x % 400 != 0:
        ebi == False
    if ebi:
        return 'eh bissexto'
    else:
        return 'nao eh bissexto'
def main():
    print("Ano bissexto ou nao\n")
    x = int(input("Ano: "))
    print(bissexto(x))
    despedida()
main()