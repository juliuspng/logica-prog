hora_inicial = int(input())
minuto_inicial = int(input())

hora_final = int(input())
minuto_final = int(input())

inicio_em_minutos = hora_inicial * 60 + minuto_inicial
final_em_minutos = hora_final * 60 + minuto_final

duracao_em_minutos = final_em_minutos - inicio_em_minutos

duracao_em_minutos = duracao_em_minutos % (24 * 60)

print(f'duração do jogo: {duracao_em_minutos // 60} horas e {duracao_em_minutos % 60} minutos')