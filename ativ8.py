#disntancia 
distan=float(input("Qual a distancia percorida em km pelo carro? "))
litros_consumidos=float(input("Qual o consumo em litros de gasolina do carro? "))

consumo=distan/litros_consumidos

if (consumo<8):
    print("Venda o carro!")
elif (consumo>8 and consumo<12):
    print("Economico!")
else:
    print("Super economico")