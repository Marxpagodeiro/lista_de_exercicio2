#energia
tipo_consu=str(input("Qual é o tipo de consumidor de energia?(digite I para industrial e C para comercial e R para recidencial) "))
energia_consu=float(input("Qual a quantidade de energia consumida? "))
industria="I"
comercial="C"
recidencial="R"

if (tipo_consu==industria):
    valor_pago=(0.68*energia_consu)+34
elif(tipo_consu==comercial):
    valor_pago=(0.37*energia_consu)+45
elif(tipo_consu==recidencial):
    valor_pago=(0.77*energia_consu)-22
print("O valor pago de energia é ",valor_pago)