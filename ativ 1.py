salario=float(input("Qual o valor do seu salario: "))
financiamento=float(input("Qual o valor do financiamento desejado: "))
valor_maximo=salario*5

if (financiamento<=valor_maximo):
    print("Financiamento concedido")
else:
    print("Financiamento negado")

print("Obrigado por nos culsultar")