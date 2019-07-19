alunosturma = int(input("Digite a quantidade de alunos que tem na turma: "))
repetição = 0
while repetição != alunosturma:
    alunos = int(input("Digite a idade de um aluno: "))
    repetição = repetição + 1
média = (alunos * repetição) / repetição
print("A media de idade dos alunos é " + str(média))
print("-------------------------Obrigado por usar meu programa! :)-------------------------")