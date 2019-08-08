from cinto_utilidades import despedida
print("Calculo de amplifitude.")
resp = 'n'
while resp == 'n':
    nums = []
    n = 1
    while n != 0:
        n = int(input("Digite um numero: "))
        nums.append(n)
        if type(n) != int:
            print("Nenhum valor informado.\n")
            nums.remove(n)
            n = int(input("Digite um numero: "))
            nums.append(n)
        if n < 0:
            print("Valor invalido\n")
            nums.remove(n) 
            n = int(input("Digite um numero: "))
            nums.append(n)          
    nums.remove(0)
    ampl = max(nums) - min(nums)
    print("\nA amplitude é " + str(ampl))
    resp = input("\nDeseja sair?s/n ")
despedida()