#calculadora velocidade de carro
dist_carroA=float(input("Qual foi a distancia percorrida pelo carroA ?"))
dist_carroB=float(input("Qual foi a distancia percorrida pelo carroB ?"))
temp_carroA=float(input("Qual foi o tempo que o carroA levou para percorrer essa distancia? "))
temp_carroB=float(input("Qual foi o tempo que o carroB levou para percorrer essa distancia? "))

velo_mediaA=dist_carroA/temp_carroA
velo_mediaB=dist_carroB/temp_carroB

if (velo_mediaA<velo_mediaB):
    print("O carroA é mais rapido que o carroB. ")
elif (velo_mediaB<velo_mediaA):
    print("O carroB é mais rapido que o carroA. ")
else:
    print("Os dois carros tem a mesma velociade ")

