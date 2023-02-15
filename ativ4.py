#numero maior 
num1=float(input("Qual o numero 1? "))
num2=float(input("Qual o numero 2? "))
num3=float(input("Qual o numero 3? "))

if (num2<num1 and num3<num1):
    print("O numero 1 é o maior ")
elif (num1<num2 and num3<num2):
    print("O numero 2 é o maior ")
else:
    print("O numero 3 é o maior ")