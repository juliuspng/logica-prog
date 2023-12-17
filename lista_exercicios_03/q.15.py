def grito_de_natal(felicidade):
    if felicidade <= 1:
        return "ta fraco"
    else:
        mensagem = "Feliz Natal"
        for _ in range(felicidade - 1):
            mensagem += "!"
        mensagem += "!!"
        return mensagem

nivel_de_felicidade = 4
mensagem_natal = grito_de_natal(nivel_de_felicidade)
print(mensagem_natal)