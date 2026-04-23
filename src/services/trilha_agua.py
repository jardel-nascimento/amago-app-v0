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


def solicitar_sim_ou_nao(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip().lower()

        if not valor:
            print("Entrada obrigatoria.")
            continue

        if valor in {"sim", "nao"}:
            return valor

        print("Digite sim ou nao.")


def executar_trilha() -> None:
    print("ETAPA ESTUDO")
    print("A agua e essencial para o funcionamento do corpo e para manter o organismo equilibrado.")
    print("Uma meta simples e consumir cerca de 2 litros de agua por dia.")
    print("Sede, cansaco e boca seca podem ser sinais de desidratacao.")

    print("ETAPA EXERCICIO")
    consumo_diario = solicitar_numero_decimal("Quanto voce bebe por dia, em litros? ")
    meta = 2.0
    esquece_agua = solicitar_sim_ou_nao("Voce costuma esquecer de beber agua? (sim/nao): ")

    print("ETAPA PRATICA")
    dia_1 = solicitar_numero_decimal("Registro de consumo - dia 1 (litros): ")
    dia_2 = solicitar_numero_decimal("Registro de consumo - dia 2 (litros): ")
    media = (dia_1 + dia_2) / 2

    print("Resumo final da trilha de hidratacao:")
    print(f"Consumo diario informado: {consumo_diario} litros")
    print(f"Meta definida: {meta} litros")
    print(f"Costuma esquecer de beber agua: {esquece_agua}")
    print(f"Media registrada nos dois dias: {media} litros")
