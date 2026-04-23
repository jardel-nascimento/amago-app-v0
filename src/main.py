def exibir_menu() -> None:
    print("1. iniciar")
    print("2. sair")


def main() -> None:
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            print("Aplicacao iniciada.")
        elif opcao == "2":
            print("Encerrando aplicacao.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
