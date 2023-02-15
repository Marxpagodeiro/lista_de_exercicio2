#jogo
hora_inicio=float(input("Qual é a hora do inicio do horario do jogo? "))
minutos_inicio=float(input("Quais são os minutos iniciais do jogo?"))
hora_fim=float(input("Qual é a hora do fim do jogo? "))
minutos_fim=float(input("Quais são os minutos no fim do jogo? "))

if(hora_inicio > 24 or hora_fim > 24):
    print("Entrada de dados em horas não é valida")
elif(minutos_inicio > 59 or minutos_fim > 59):
    print("Entrada de dados em minutos não é valida")

elif(hora_inicio > hora_fim):
    duracao_horas = hora_fim - hora_inicio +24
    if(minutos_inicio > minutos_fim):
        duracao_horas = duracao_horas - 1
        duracao_m = minutos_fim - minutos_inicio + 60
        print("Se passaram: ", duracao_horas, "horas,", duracao_m, "minutos.")
    else:
        duracao_m = minutos_fim - minutos_inicio
        print("Se passaram: ", duracao_horas, "horas,", duracao_m, "minutos.")

elif(hora_inicio < hora_fim):
    duracao_horas = hora_fim - hora_inicio
    if(minutos_inicio > minutos_fim):
        duracao_horas = duracao_horas - 1
        duracao_m = minutos_fim - minutos_inicio + 60
        print("Se passaram: ", duracao_horas, "horas,", duracao_m, "minutos.")
    else:
        duracao_m = minutos_fim - minutos_inicio
        print("Se passaram: ", duracao_horas, "horas,", duracao_m, "minutos.")