print("1 - Mercurio")
print("2 - Venus")
print("3 - Marte")
print("4 - Jupiter")
print("5 - Saturno")
print("6 - Urano")
plant = int(input("Digite o numero correspondente ao planeta que queira converter seu peso: "))
peso = float(input("Digite seu peso: "))
if plant == 1:
    pesoM = peso * 0.37
    print("O seu peso em Mercurio é " + str(pesoM))
elif plant == 2:
    pesoV = peso * 0.88
    print("O seu peso em Venus é " + str(pesoV))
elif plant == 3:
    pesoMt = peso * 0.38
    print("O seu peso em Marte é " + str(pesoMt))
elif plant == 4:
    pesoJ = peso * 2.64
    print("O seu peso em Jupiter é " + str(pesoJ))
elif plant == 5:
    pesoS = peso * 1.15
    print("O seu peso em Saturno é " + str(pesoS))
elif plant == 6:
    pesoU = peso * 1.17
    print("O seu peso em Urano é " + str(pesoU))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")