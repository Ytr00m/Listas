ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    bissexto = ano & 100 != 0
    print("O ano é bissexto")
else:
    if ano % 4 != 0:
        if ano % 400 != 0:
            print("O ano não é bissexto")
        else:
            if ano % 4 != 0:
                if ano % 400 == 0:
                    print("O ano é bissexto")
print("-------------------------Obrigado por usar meu programa! :)-------------------------")
