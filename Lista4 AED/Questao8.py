num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais um numero: "))
if num1 > num2 and num1 > num3:
    print("O maior numero é " + str(num1))
else:
    if num2 > num1 and num2 > num3:
        print("O maior numero é " + str(num2))
    else:
        if num3 > num1 and num3 > num2:
            print("O maior numero é " + str(num3))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")