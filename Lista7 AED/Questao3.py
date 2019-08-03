from cinto_utilidades import despedida
def porcento(x, y):
    return (x * 100) / y
loop = True
votoch1 = 0
votoch2 = 0
votobra = 0
votonull = 0
while loop == True:
    print("0 - Sair do Programa")
    print("1 - Chapa 1")
    print("2 - Chapa 2")
    print("3 - Voto em branco")
    print("4 - Voto nulo")
    ação = int(input("O que deseja fazer? "))
    print("Feito")
    print("------------------------------------")
    if ação == 0:
        break
    elif ação != 0 and ação != 1 and ação != 2 and ação != 3 and ação != 4:
        print("Você deve responder de acordo com o que foi pedido")
        print("------------------------------------")
    elif ação == 1:
        votoch1 += 1
    elif ação == 2:
        votoch2 += 1
    elif ação == 3:
        votobra += 1
    elif ação == 4:   
        votonull += 1
votos = [votobra, votoch1, votoch2, votonull]
print("Chapa 1: " + str(votoch1))
print("Chapa 2: " + str(votoch2))
print("Brancos e nulos: " + str(votobra + votonull))
soma = votobra + votonull + votoch2 + votoch1
maxx = max(votos)
if votoch1 == votoch2:
    print("Ouve um empate")
if maxx == votoch1:
    por = porcento(votoch1, soma)
    print("A chapa vencedora é a 1 com " + str(por) + " por cento dos votos")
elif maxx == votoch2:
    por2 = porcento(votoch2, soma)
    print("A chapa vencedora é a 2 com " + str(por2) + " por cento dos votos")
despedida()