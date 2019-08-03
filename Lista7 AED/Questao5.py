from cinto_utilidades import despedida
numero = 1
seq = []
while numero != 0:
    numero = int(input("Digite um numero da sequencia ou zero para termina-la: "))
    seq .append(numero)
seq.remove(0)
maximo = max(seq)
num = 0
i = 0
for suma in seq:
    num = num + seq[i]
    i = i + 1
qnt = len(seq)
média = num / qnt
print("Média: " + str(média))
print("Maior valor: " + str(maximo))
despedida()
