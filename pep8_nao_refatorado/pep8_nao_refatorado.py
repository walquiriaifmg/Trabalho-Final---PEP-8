x = []

while True:
    print("\n===== AGENDA DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar pendências")
    print("4 - Listar todas as tarefas")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        a = input("Digite a tarefa: ")
        b = {"n": a, "c": False}
        x.append(b)
        print("Tarefa cadastrada!")

    elif op == "2":
        if len(x) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i in range(len(x)):
                print(i + 1, "-", x[i]["n"])

            y = int(input("Número da tarefa concluída: "))

            if y >= 1 and y <= len(x):
                x[y - 1]["c"] = True
                print("Tarefa concluída!")
            else:
                print("Número inválido.")

    elif op == "3":
        print("\nPendências:")
        z = False

        for t in x:
            if t["c"] == False:
                print("-", t["n"])
                z = True

        if z == False:
            print("Não há tarefas pendentes.")

    elif op == "4":
        if len(x) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for t in x:
                if t["c"] == True:
                    print(t["n"], "- Concluída")
                else:
                    print(t["n"], "- Pendente")

    elif op == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")