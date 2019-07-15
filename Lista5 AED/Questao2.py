a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
if a > b and a > c and b > c:
    print("Decrescente: " + str(a) + " " + str(b) + " " + str(c))
else:
    if a > b and a > c and b < c:
        print("Decrescente: " + str(a) + " " + str(c) + " " + str(b))
    else:
        if b > a and b > c and a > c:
            print("Decrescente: " + str(b) + " " + str(a) + " " + str(c))
        else:
            if b > a and b > c and a < c:
                print("Decrescente: " + str(b) + " " + str(c) + " " + str(a))
            else:
                if c > a and c > b and b > a:
                    print("Decrescente: " + str(c) + " " + str(b) + " " + str(a))
                else:
                    if c > a and c > b and b < a:
                        print("Decrescente: " + str(c) + " " + str(a) + " " + str(b))
print("-------------------------Obrigado por usar meu programa! :)-------------------------") 