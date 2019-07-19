loop = True
while loop == True:
    print("0 para sair do programa")
    print("1 para adição")
    print("2 para subtração")
    print("3 para multiplicação")
    print("4 para divisão\n")
    resp = int(input("O que deseja fazer? "))
    if resp == 0:
        loop = False
        print("Obrigado por usar este programa!")
    else:
        if resp == 1:
            num1Ad = int(input("Digite o primeiro numero da operação: "))
            num2Ad = int(input("Digite o segundo numero da operação: "))
            resultadoAd = num1Ad + num2Ad
            print("O resultado é " + str(resultadoAd))
            print("--------------------------------------------")
        else:
            if resp == 2:
                num1Sub = int(input("Digite o primeiro numero da operação: "))
                num2Sub = int(input("Digite o segundo numero da operação: "))
                resultadoSub = num1Sub - num2Sub
                print("O resultado é " + str(resultadoSub))
                print("--------------------------------------------")
            else:
                if resp == 3:
                    num1Mult = int(input("Digite o primeiro numero da operação: "))
                    num2Mult = int(input("Digite o segundo numero da operação: "))
                    resultadoMult = num1Mult * num2Mult
                    print("O resultado é " + str(resultadoMult))
                    print("--------------------------------------------")
                else:
                    if resp == 4:
                        num1Div = int(input("Digite o primeiro numero da operação: "))
                        num2Div = int(input("Digite o segundo numero da operação: "))
                        resultadoDiv = num1Div / num2Div
                        print("O resultado é " + str(resultadoDiv))
                        if num1Div % num2Div != 0:
                            resto = num1Div % num2Div
                            print("e o resto é " + str(resto))
                            print("--------------------------------------------")