from cinto_utilidades import despedida
def FETUCCINE(termo1, termo2):
    fetucci = []
    a1 = termo1
    a2 = termo2
    count = 2
    while len(fetucci) != 100:
        a1 = (a1-1) + (a1-2)
        fetucci.append(a1)
        a2 = (a2-1) - (a2-2)
        fetucci.append
    return fetucci
print("100 primeiros termos da serie FETUCCINE.\n")
termo1 = int(input("Digite o primeiro termo: "))
termo2 = int(input("Digite o segundo termo: "))
print(FETUCCINE(termo1, termo2))
despedida()