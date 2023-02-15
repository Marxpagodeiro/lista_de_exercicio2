#atividade16
algo=float(input("Digite um algoritmo inteiro de tres digitos? "))

#calculo da soma dos tres digitos
algo1 = algo // 1 % 10
algo2 = algo // 10 % 10
algo3 = algo // 100 % 10
std=algo1+algo2+algo3
multiplo=std%4


if (std == 1 or std == 2 or std == 4 or std == 8 or std == 16):
    if(multiplo == 0):
        print("O número é divisor de 16 e múltiplo de 4 ao mesmo tempo.")
else:
    print("O número não é divisor de 16 e múltiplo de 4 ao mesmo tempo.")