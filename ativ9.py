#calculadora de caloria
sexo=str(input("Qual o seu sexo? (responder M para masculino e F para feminino)"))
Peso=float(input("Qual é o seu peso? ")) 
altura=float(input("Qual é o sua altura? "))
idade=float(input("Qual é o sua idade? "))
sex1="M"
sex2="F"

if(sexo==sex1):
    consumo_caloriasM=66+(13.7*Peso)+(5*altura)-(6.8*idade)
    print("O cunsumo de calorias ideal dessa pessoa é ",consumo_caloriasM)
elif(sexo==sex2):
    consumo_caloriasF=665+(9.6*Peso)+(1.8*altura)-(4.7*idade)
    print("O cunsumo de calorias ideal dessa pessoa é ",consumo_caloriasF)