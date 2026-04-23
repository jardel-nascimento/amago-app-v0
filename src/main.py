import os

from services.anamnese import coletar_anamnese
from services.trilha_agua import executar_trilha
from ui.app import AmagoApp


def exibir_menu() -> None:
    print("1. iniciar")
    print("2. sair")


def main() -> None:
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            respostas = coletar_anamnese()
            print("Resumo da anamnese:")
            print(f"Idade: {respostas['idade']}")
            print(f"Peso: {respostas['peso']}")
            print(f"Consumo de agua: {respostas['consumo_agua']}")
            executar_trilha()
        elif opcao == "2":
            print("Encerrando aplicacao.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    if os.environ.get("ANDROID_ARGUMENT"):
        AmagoApp().run()
    else:
        main()
