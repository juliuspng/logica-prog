lista_de_tarefas = []
def adicionar_tarefa(tarefa):
    global lista_de_tarefas
    lista_de_tarefas.append(tarefa)
    print(f"tarefa '{tarefa}' adicionada com sucesso!")

def exibir_tarefas():
    global lista_de_tarefas
    if not lista_de_tarefas:
        print("lista de tarefas está vazia.")
    else:
        print("lista de Tarefas:")
        for i, tarefa in enumerate(lista_de_tarefas, start=1):
            print(f"{i}. {tarefa}")

adicionar_tarefa("assistir manifesto comunista 2")
adicionar_tarefa("assistir entre irmãos ")
adicionar_tarefa("assistir krampus")
adicionar_tarefa("assistir assim na terra")
adicionar_tarefa("assistir rick and morty")

exibir_tarefas()