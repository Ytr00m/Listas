from cinto_utilidades import despedida
def Fibonacci(n):
    fibonac = [0, 1]
    a1 = 0
    a2 = 1
    count = 1
    while count < n:
        sucessor = fibonac[a1] + fibonac[a2]
        fibonac.append(sucessor)
        a1 += 1
        a2 += 1
        count += 1
    return fibonac
n = int(input("Digite quantos termos Fibonacci que quer: "))
seq = Fibonacci(n)
print(seq)
despedida()