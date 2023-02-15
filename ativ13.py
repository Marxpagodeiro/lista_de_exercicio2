#hastes
hastes_aco=float(input("Quantas hastes de aço vão ser compradas? "))
hastes_cu=float(input("Quantas hastes de cobre vão ser compradas? "))
hastes_alu=float(input("Quantas hastes de aluminio vão ser compradas? "))

valor_total=(hastes_aco*2.50)+(hastes_cu*4)+(hastes_alu*5)
quantidade_total_hastes= hastes_aco+hastes_cu+hastes_alu

if(quantidade_total_hastes<=6):
    desconto=0
    total_pago=valor_total-desconto
    print("não tem desconto")
elif(quantidade_total_hastes>=7 and quantidade_total_hastes<=15):
    desconto=valor_total*0.10
    total_pago=valor_total-desconto
elif(quantidade_total_hastes>=16 and quantidade_total_hastes<=20):
    desconto=valor_total*0.15
    total_pago=valor_total-desconto
else:
    desconto=valor_total*0.20
    total_pago=valor_total-desconto
print("O valor total da compra foi",total_pago)



