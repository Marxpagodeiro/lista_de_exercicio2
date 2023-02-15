#leiotor de mes 
mes = float(input("Digite o número do mês: "))
ano = float(input("Digite o ano: "))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    if(mes==1):
        print("31 dias")
    elif (mes == 2):
        print("29 dias")
    elif(mes==3):
        print("31 dias")
    elif(mes==4):
        print("30 dias")
    elif(mes==5):
        print("31 dias")
    elif(mes==6):
        print("30 dias")
    elif(mes==7):
        print("31 dias")
    elif(mes==8):
        print("31 dias")
    elif(mes==9):
        print("30 dias")
    elif(mes==10):
        print("31 dias")
    elif(mes==11):
        print("30 dias")
    elif(mes==12):
        print("31 dias")

else:
    if(mes==1):
        print("31 dias")
    elif (mes == 2):
        print("28 dias")
    elif(mes==3):
        print("31 dias")
    elif(mes==4):
        print("30 dias")
    elif(mes==5):
        print("31 dias")
    elif(mes==6):
        print("30 dias")
    elif(mes==7):
        print("31 dias")
    elif(mes==8):
        print("31 dias")
    elif(mes==9):
        print("30 dias")
    elif(mes==10):
        print("31 dias")
    elif(mes==11):
        print("30 dias")
    elif(mes==12):
        print("31 dias")