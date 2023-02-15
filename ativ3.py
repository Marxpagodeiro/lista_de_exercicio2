#idade 
nome1=str(input("Qual o nome do primeiro sujeito? "))
nome2=str(input("Qual o nome do segundo sujeito? "))
idade1=float(input("Qual a idade do primeiro sujeito? "))
idade2=float(input("Qual a idade do segundo sujeito? "))

# calculadora de ano
ano_atual=2023
ano_nasci1=ano_atual-idade1
ano_nasci2=ano_atual-idade2

if (idade1<idade2):
    print(nome1,(" é mais novo que "),nome2,(" e nasceu no ano de "),ano_nasci1 )
elif (idade2<idade1):
    print(nome2,(" é mais novo que "),nome1,(" e nasceu no ano de "),ano_nasci2 )
else:
    print(nome1,(" tem a mesma idade que "),nome2,(" e ambos nasceram no ano de "),ano_nasci1 )
