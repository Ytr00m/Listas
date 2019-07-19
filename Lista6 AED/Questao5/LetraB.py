ano1 = int(input("Digite um ano para vermos se é bissexto ou não: "))
if ano1 % 4 == 0 and ano1 % 100 != 0:
    print("Este ano é bissexto")
elif ano1 % 4 != 0 and ano1 % 400 != 0:
    print("Este ano não é bissexto")
elif ano1 % 4 != 0 and ano1 % 400 == 0:
    print("Este ano é bissexto")
resp = input("Você deseja verificar outro ano?(s/n) ")

while resp != 's' and resp != 'n':
    print("Ta cego tio, é pra responder 's' ou 'n'")
    resp = input("Resp: ")
if resp == 's':
    ano2 = int(input("Qual? "))
    if ano2 % 4 == 0 and ano2 % 100 != 0:
        print("Este ano é bissexto")
    if ano2 % 4 != 0 and ano2 % 400 != 0:
        print("Este ano não é bissexto")
    if ano2 % 4 != 0 and ano2 % 400 == 0:
        print("Este ano é bissexto")
else:
    print("Talkey!")
print("-------------------------Obrigado por usar meu programa! :)-------------------------")