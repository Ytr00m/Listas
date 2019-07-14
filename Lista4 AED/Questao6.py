from math import sqrt
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b ** 2 - 4 * a * c
raizdelta = sqrt(b ** 2 - 4 * a * c)
x1 = (-b + raizdelta) / (2 * a)
x2 = (-b - raizdelta) / (2 * a)
print("x1 = " + str(x1))
print("x2 = " +str(x2))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")