from math import sqrt

abscissaA = int(input("Digite a abscissa do ponto a: "))
abscissaB = int(input("Digite a abscissa do ponto b: "))
ordenadaA = int(input("Digite a ordenada do ponto a: "))
ordenadaB = int(input("Digite a ordenada do ponto b: "))
dist = sqrt((abscissaA - abscissaB) + (ordenadaA - ordenadaB))
print("A distancia do ponto a para o ponto b é de " + str(dist))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")