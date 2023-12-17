def adicionar_contato(agenda):
    contato = []
    nome = input("digite o nome do contato: ")
    telefone = input("digite o número de telefone: ")
    contato.append(nome)
    contato.append(telefone)
    agenda.append(contato)
    print("contato adicionado com sucesso!")

def buscar_contato(agenda):
    nome = input("digite o nome do contato: ")
    encontrado = False
    for contato in agenda:
        if contato[0] == nome:
            print(f"O número de telefone de {nome} é: {contato[1]}")
            encontrado = True
            break
    if not encontrado:
        print(f"{nome} não encontrado na agenda.")

def exibir_menu():
    print("\nagenda de Contatos:")
    print("1. adicionar Contato")
    print("2. buscar Contato")
    print("3. sair")

def main():
    agenda = []
    
    while True:
        exibir_menu()
        escolha = input("escolha uma opção: ")

        if escolha == "1":
            adicionar_contato(agenda)
        elif escolha == "2":
            buscar_contato(agenda)
        elif escolha == "3":
            print("saindo...")
            break
        else:
            print("opção inválida. tente novamente.")

if __name__ == "__main__":
    main()