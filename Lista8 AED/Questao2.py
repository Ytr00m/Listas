from cinto_utilidades import despedida
print("Calculo de fatorial.")
n = int(input("Numero: "))
if n == 0:
    print("Fatorial: 1")
else:
    num = n
    rest = n - 1
    for i in range(0, num-1):
        n *= rest
        rest -= 1
    print("Fatorial: " + str(n))
despedida()