prova1 = int(input("Valor obtido na primeira prova valendo 50: "))
prova2 = int(input("Valor obtido na segunda prova valendo 50: "))
ntfinal = prova1 + prova2
if ntfinal >= 60:
    print("Parabéns, você foi aprovado")
elif ntfinal >= 40 and ntfinal < 60:
    print("Você ficou em reavaliação")
elif ntfinal < 40:
    print("Infelizmente você foi reprovado")
