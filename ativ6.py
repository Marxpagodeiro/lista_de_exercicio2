#reprovação por nota
media_aluno=float(input("Qual é a media do aluno(de 0 a 10)? "))
faltas_aluno=float(input("Qual é o numero de faltas do aluno? "))

#consições
if (media_aluno>=7 and faltas_aluno<=32):
    print("O aluno foi aprovado")
elif (media_aluno<=7 and faltas_aluno<=32):
    print("O aluno foi reprovado por media")
elif (media_aluno>=7 and faltas_aluno>=32):
    print("O aluno foi reprovado por falta")
else:
    print("O aluno foi reprovado por falta e por media")