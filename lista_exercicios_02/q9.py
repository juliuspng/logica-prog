#a.
import random
#b.
opcao_computador = random.randint(0, 2)
#c.
if opcao_computador == 0:
    escolha_computador = 'pedra'
elif opcao_computador == 1:
    escolha_computador = 'papel'
else:
    escolha_computador = 'tesoura'
#o else faz o papel do 2

#d.
opcao_jogador = input("Escolha: pedra, papel ou tesoura? ")

#e.
if (opcao_jogador == 'pedra' and escolha_computador == 'tesoura') or \
   (opcao_jogador == 'tesoura' and escolha_computador == 'papel') or \
   (opcao_jogador == 'papel' and escolha_computador == 'pedra'):
    print(f'Jogador venceu! Computador escolheu {escolha_computador}.')

#f.
else:
    print(f'Computador venceu! Computador escolheu {escolha_computador}.')  

#g.
if opcao_jogador == escolha_computador:
    print(f'Empate! Ambos escolheram {escolha_computador}.') 