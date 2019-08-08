from cinto_utilidades import despedida
print("Termos divisiveis por x em uma progressao aritmetica.")
resp = 'entrar'
while resp != 's':
    termos = int(input("\nDigite o numero de termos da PA: "))
    razao = int(input("Digite a razao: "))
    termos *= razao
    PA = list(range(0, termos+1, razao))
    PA.remove(0)
    x = float(input("Digite o divisor: "))
    divi = 0
    for i in PA:
        if i % x == 0:
            divi += 1
    print("\nExistem " + str(divi) + " termos divisiveis por " + str(x) + " nesta PA.\n")
    resp = input("Deseja sair?s/n ")
despedida()