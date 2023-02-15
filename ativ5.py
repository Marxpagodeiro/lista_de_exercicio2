#Nota dos alunos
aluno=str(input("Qual o nome do aluno? "))
nota1=float(input("Qual é a nota do aluno(de 0 a 10)? "))
nota2=float(input("Qual é a nota do aluno(de 0 a 10)? "))

#media das notas
media=(nota1+nota2)/2

if (media>=7 and media<=10):
    print("O aluno",aluno,"de media ",media,"esta aprovado.")
elif (media>=5 and media<=7):
    print("O aluno",aluno,"de media ",media,"esta de recuperação.")
else:
    print("O aluno",aluno,"de media ",media,"esta reprovado.")