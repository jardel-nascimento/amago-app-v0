def solicitar_numero_inteiro(mensagem: str) -> int:
    while True:
        valor = input(mensagem).strip()

        if not valor:
            print("Entrada obrigatoria.")
            continue

        try:
            return int(valor)
        except ValueError:
            print("Digite um numero inteiro valido.")


def solicitar_numero_decimal(mensagem: str) -> float:
    while True:
        valor = input(mensagem).strip()

        if not valor:
            print("Entrada obrigatoria.")
            continue

        try:
            return float(valor)
        except ValueError:
            print("Digite um numero valido.")


def solicitar_consumo_agua() -> str:
    opcoes_validas = {"baixo", "medio", "alto"}

    while True:
        valor = input("Consumo de agua (baixo, medio, alto): ").strip().lower()

        if not valor:
            print("Entrada obrigatoria.")
            continue

        if valor in opcoes_validas:
            return valor

        print("Informe uma opcao valida: baixo, medio ou alto.")


def coletar_anamnese() -> dict:
    return {
        "idade": solicitar_numero_inteiro("Idade: "),
        "peso": solicitar_numero_decimal("Peso: "),
        "consumo_agua": solicitar_consumo_agua(),
    }
