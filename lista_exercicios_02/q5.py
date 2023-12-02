numerodomes= int(input("digite um valor inteiro de 1 a 12: "))

if 1 <= numerodomes <= 12:
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#vou usar lista

mes_extenso = meses[numerodomes - 1]
print(f"o mês correspondente é: {mes_extenso}")
