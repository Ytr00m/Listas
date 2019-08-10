from cinto_utilidades import despedida
print("Calculo de itens defeituosos.\n")
maq, produtos, defei = 1, [], []
for i in range(0, 5):
    produto = int(input("Digite o numero de produtos gerados pela {} maquina: ".format(maq)))
    defi = int(input("e dos defeituosos? "))
    produtos.append(produto)
    defei.append(defi)
    maq += 1
indi, pores = 0, []
for i in range(0, 5):
    porerros = (defei[indi] * 100) / produtos[indi]
    pores.append(porerros)
    indi += 1
maqmaiser = max(pores)
if maqmaiser == pores[0]:
    print("A maquina com mais produtos defeituosos foi a primeira com {}.".format(defei[0]))
elif maqmaiser == pores[1]:
    print("A maquina com mais produtos defeituosos foi a segunda com {}.".format(defei[1]))
elif maqmaiser == pores[2]:
    print("A maquina com mais produtos defeituosos foi a terceira com {}.".format(defei[2]))
elif maqmaiser == pores[3]:
    print("A maquina com mais produtos defeituosos foi a quarta com {}.".format(defei[3]))
elif maqmaiser == pores[4]:
    print("A maquina com mais produtos defeituosos foi a quinta com {}.".format(defei[4]))
despedida()
