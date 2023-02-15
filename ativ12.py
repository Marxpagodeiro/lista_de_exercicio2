#Maioridade
sexo=str(input("Qual o seu sexo? (responder M para masculino e F para feminino)"))
idade=float(input("Qual é o sua idade? "))
sex1="M"
sex2="F"

if(sexo==sex1 and idade>=21):
    print("A pessoa em questão é de maior")
elif(sexo==sex2 and idade>=18):
    print("A pessoa em questão é de maior")
else:
    print("A pessoa em questão é de menor")