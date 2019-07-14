lado1 = int(input("Digite um lado de um tringulo: "))
lado2 = int(input("Digite mais um lado de um tringulo: "))
lado3 = int(input("Digite outro lado de um tringulo: "))
if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("Este triangulo é equilatero")
else:
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Este triangulo é isósceles")
    else:
        print("Este triangulo é escaleno")

print("-------------------------Obrigado por usar meu programa! :)-------------------------")
