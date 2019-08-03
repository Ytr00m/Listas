from cinto_utilidades import despedida
h = int(input("Digite o numero de termos: "))
num = 100
i = num / h
soma = 0
count = h
while count > 0:
    H = 0
    i = h / num + soma
    num -= 3
    soma = i
    H += i
    count -= 1
print("O valor de H é: " + str(H))
despedida()