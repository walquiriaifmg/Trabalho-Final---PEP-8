from menu import exibir_menu

from tarefas import (
    cadastrar_tarefa,
    concluir_tarefa,
    listar_pendencias,
    listar_tarefas
)


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


if __name__ == "__main__":
    main()