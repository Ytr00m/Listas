from cinto_utilidades import despedida
n = int(input("Digite quantos termos quer: "))
num = 1
div = 100
while n > 0:
    divi = num / div
    print(divi)
    num += 1
    div -= 3
    n -= 1
despedida()