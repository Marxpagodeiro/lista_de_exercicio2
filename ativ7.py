#triangulo angulos
an1=float(input("Qual o valor do primeiro angulo? "))
an2=float(input("Qual o valor do segundo angulo? "))
an3=float(input("Qual o valor do terceiro angulo? "))

#confirmação de triangulo
triangulo=an1+an2+an3

#condições 
if (triangulo==180):
    print("A figura é um triangulo ")
    if(an1<90 and an2<90 and an3<90):
        print("A figura é um triangulo acutângulo ")
    elif(an1==90 or an2==90 or an3==90):
        print("A figura é um triangulo retângulo ")
    elif(an1>90 or an2>90 or an3>90):
        print("A figura é um triangulo obtusângulo ") 
else:
    print("Os ângulos informados não formam um triângulo ")