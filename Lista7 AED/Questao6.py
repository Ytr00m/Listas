from cinto_utilidades import despedida
aluno = int(input("Digite o numero de alunos que tem na turma: "))
count = 0
idadalunos = []
maioresidad = []
while count < aluno:
    idad = int(input("Digite a idade de um dos alunos: "))
    idadalunos.append(idad)
    if idad >= 18:
        maioresidad.append(idad)
        idadalunos.remove(idad)
        if idad > 100:
            maioresidad.remove(idad)
    count += 1
poralunosmaio = (len(maioresidad) * 100) / (len(idadalunos) + len(maioresidad))
idadpemaisve = max(idadalunos + maioresidad)
idadepmaisno = min(idadalunos + maioresidad)
print(str(poralunosmaio) + " porcento dos alunos são maiores de idade.")
print("A pessoa mais velha tem " + str(idadpemaisve) + " anos de idade.")
print("A pessoa mais nova tem " + str(idadepmaisno) + " anos de idade.")
despedida()



