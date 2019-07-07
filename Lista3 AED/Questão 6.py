import datetime
hoje = datetime.date.today()
anoAtual = int(hoje.strftime("%Y"))
meses = {  1 : 'janeiro' , 2 : 'fevereiro' , 3 : 'marco', 4 : 'abril' , 5 : 'maio' , 6 : 'junho', 7 : 'julho', 8 : 'agosto' , 9 : 'setembro' , 10 : 'outubro' , 11 : 'novembro' , 12 : 'dezembro' }

bissexto = False
dia = int(input("Digite um dia correspondente ao seu nascimento: "))
mes = int(input("Digite um mes correnspondente ao do seu nascimento: "))
ano = int(input("Digite o ano corresponde ao do seu nascimento (a partir de 1583 \n Ex: 1990 \n "))
if ano < 1583:
    print("Não é possivel calcular para antes de 1583, pois nao usavamos o mesmo calendario que hoje")

if ano > anoAtual:
    print("Olá, pelo visto você é do futuro")
niver = datetime.date(ano, mes , dia)
idadeemdias = hoje - niver
print("Voçê ja viveu " + str(idadeemdias))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")

   
        
