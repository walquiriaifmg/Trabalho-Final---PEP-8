def cadastrar_tarefa(tarefas):
    nome = input("Digite a tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print("Tarefa cadastrada!")


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice} - {tarefa['nome']}")

    numero = int(input("Número da tarefa concluída: "))

    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa concluída!")
    else:
        print("Número inválido.")


def listar_pendencias(tarefas):
    encontrou = False

    print("\nPendências:")

    for tarefa in tarefas:
        if not tarefa["concluida"]:
            print(f"- {tarefa['nome']}")
            encontrou = True

    if not encontrou:
        print("Não há tarefas pendentes.")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{tarefa['nome']} - {status}")


def exibir_menu():
    print("\n===== AGENDA DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar pendências")
    print("4 - Listar todas as tarefas")
    print("0 - Sair")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            concluir_tarefa(tarefas)

        elif opcao == "3":
            listar_pendencias(tarefas)

        elif opcao == "4":
            listar_tarefas(tarefas)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


main()