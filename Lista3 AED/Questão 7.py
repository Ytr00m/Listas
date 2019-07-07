from math import sqrt
a = int(input("Digite o primeiro termo da equação de segundo grau: "))
b = int(input("Digite o segundo termo da equação de segundo grau: "))
c = int(input("Digite o terceiro termo da equação de segundo grau: "))
delta = b ** 2 -4 * a * c
raizdelta = sqrt(delta)
x1 = (-b + raizdelta) / (2 * a)
x2 = (-b - raizdelta) / (2 * a)
print("Delta: " + str(delta))
print("Raiz de delta: " + str(raizdelta))
print("x1: " + str(x1))
print("x2: " + str(x2))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")
