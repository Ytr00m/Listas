from cinto_utilidades import despedida
print("Calculo da media de notas.\n")
nota, apro, repro = 0, [], []
while nota != -1:
    nota = int(input("Digite a nota de um aluno:(menor ou igual a 100 ou -1 para finalizar a leitura) "))
    if nota > 100:
        while nota > 100:
            print("\nValor invalido!")
            nota = int(input("\nDigite a nota de um aluno:(menor ou igual a 100 ou -1 para finalizar a leitura) "))
    if nota >= 60:
        apro.append(nota)
    if nota < 60:
        repro.append(nota)
repro.remove(-1)
if len(apro) == 0:
    notarepro, count, aprofor, reprofor = 0, 0, len(apro), len(repro)
    for i in range(0, reprofor):
        notarepro += repro[count]
        count += 1
    mediarepro = notarepro / len(repro)
    print("\nA nota media dos alunos reprovados é de {} pontos.".format(int(mediarepro)))
    print("Nenhum aluno foi aprovado nesta turma.")
    despedida()
if len(repro) == 0:
    notapro, count, aprofor, reprofor = 0, 0, len(apro), len(repro)
    for i in range(0, aprofor):
        notapro += apro[count]
        count += 1
    mediapro = notapro / len(apro)
    print("\nA nota media dos alunos aprovados é de {} pontos.".format(int(mediapro)))
    print("Nenhum aluno foi reprovado nesta turma.")
    despedida()
elif len(repro) > 0 and len(apro) > 0:
    notapro, count, aprofor, reprofor = 0, 0, len(apro), len(repro)
    for i in range(0, aprofor):
        notapro += apro[count]
        count += 1
    notarepro, count = 0, 0
    for i in range(0, reprofor):
        notarepro += repro[count]
        count += 1
    mediapro = notapro / len(apro)
    mediarepro = notarepro / len(repro)
    print("\nA nota media dos alunos reprovados é de {} pontos.".format(int(mediarepro)))
    print("A nota media dos alunos aprovados é de {} pontos.".format(int(mediapro)))
    despedida()