from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


def simular_anamnese() -> dict:
    return {
        "idade": 25,
        "peso": 70.0,
        "consumo_agua": "medio",
    }


def simular_trilha_agua() -> dict:
    consumo_diario = 1.5
    meta = 2.0
    esquece_agua = "sim"
    dia_1 = 1.8
    dia_2 = 2.1
    media = (dia_1 + dia_2) / 2

    return {
        "consumo_diario": consumo_diario,
        "meta": meta,
        "esquece_agua": esquece_agua,
        "dia_1": dia_1,
        "dia_2": dia_2,
        "media": media,
    }


class AmagoApp(App):
    def build(self) -> BoxLayout:
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.resultado = Label(
            text="Aplicativo Amago v0\nClique em Iniciar para simular a anamnese e a trilha de agua.",
            halign="left",
            valign="middle",
        )
        self.resultado.bind(size=self._ajustar_texto)

        botao_iniciar = Button(text="Iniciar", size_hint=(1, 0.2))
        botao_iniciar.bind(on_press=self.executar_fluxo)

        layout.add_widget(self.resultado)
        layout.add_widget(botao_iniciar)
        return layout

    def _ajustar_texto(self, *_args) -> None:
        self.resultado.text_size = self.resultado.size

    def executar_fluxo(self, _instance) -> None:
        anamnese = simular_anamnese()
        trilha = simular_trilha_agua()

        self.resultado.text = (
            "Resumo do app:\n"
            f"Idade: {anamnese['idade']}\n"
            f"Peso: {anamnese['peso']}\n"
            f"Consumo de agua: {anamnese['consumo_agua']}\n"
            f"Consumo diario: {trilha['consumo_diario']} litros\n"
            f"Meta: {trilha['meta']} litros\n"
            f"Esquece de beber agua: {trilha['esquece_agua']}\n"
            f"Dia 1: {trilha['dia_1']} litros\n"
            f"Dia 2: {trilha['dia_2']} litros\n"
            f"Media: {trilha['media']} litros"
        )


if __name__ == "__main__":
    AmagoApp().run()
