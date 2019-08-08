from cinto_utilidades import despedida
print("Calculo de potencia:")
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
rest = 1
for i in range(0, expoente):
    rest *= base

print("A potencia é: " + str(rest))
despedida()

