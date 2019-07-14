genero = int(input("Qual é seu sexo?(1 para f/2 para m) "))
if genero == 1:
    alturaf = float(input("Digite sua altura: "))
    pesoIdealf = (62.1 * alturaf) - 44.7
    print("Seu peso ideal é " + str(pesoIdealf))
else:
    alturam = float(input("Digite sua altura: "))
    pesoIdealm = (72.7 * alturam) - 58
    print("Seu peso ideal é " + str(pesoIdealm))

print("-------------------------Obrigado por usar meu programa! :)-------------------------")