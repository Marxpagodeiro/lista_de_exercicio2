#IMPOSTO RENDA
salario_bruto=float(input("Qual é o seu salario bruto ? "))

if (salario_bruto<1903.98):
    irrf=0
    salario_liquido=salario_bruto-irrf
    print("Você esta isento de pagar imposto de renda")
    print("Com base no seu salario bruto",salario_bruto," o valor do desconto do IRRF é",irrf," e o valor do seu salario liquido é ",salario_liquido)
elif(salario_bruto>1903.98 and salario_bruto<=2826.65):
    irrf=(salario_bruto*0.075)-142.80
    salario_liquido=salario_bruto-irrf
    print("Com base no seu salario bruto",salario_bruto," o valor do desconto do IRRF é",irrf," e o valor do seu salario liquido é ",salario_liquido)
elif(salario_bruto>=2826.66 and salario_bruto<=3751.05):
    irrf=(salario_bruto*0.15)-548.82
    salario_liquido=salario_bruto-irrf
    print("Com base no seu salario bruto",salario_bruto," o valor do desconto do IRRF é",irrf," e o valor do seu salario liquido é ",salario_liquido)
elif(salario_bruto>=3751.06 and salario_bruto<=4664.68):
    irrf=(salario_bruto*0.225)-636.13
    salario_liquido=salario_bruto-irrf
    print("Com base no seu salario bruto",salario_bruto," o valor do desconto do IRRF é",irrf," e o valor do seu salario liquido é ",salario_liquido)
else:
    irrf=(salario_bruto*0.275)-869.36
    salario_liquido=salario_bruto-irrf
    print("Com base no seu salario bruto",salario_bruto," o valor do desconto do IRRF é",irrf," e o valor do seu salario liquido é ",salario_liquido)    