from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class AmagoApp(App):
    def build(self) -> BoxLayout:
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.idade_input = TextInput(hint_text="Idade", multiline=False)
        self.peso_input = TextInput(hint_text="Peso", multiline=False)
        self.consumo_agua_input = TextInput(
            hint_text="Consumo de agua (baixo, medio, alto)",
            multiline=False,
        )

        self.resultado = Label(
            text="Aplicativo Amago v0\nPreencha os campos e clique em Iniciar.",
            halign="left",
            valign="middle",
        )
        self.resultado.bind(size=self._ajustar_texto)

        botao_iniciar = Button(text="Iniciar", size_hint=(1, 0.2))
        botao_iniciar.bind(on_press=self.executar_fluxo)

        layout.add_widget(self.idade_input)
        layout.add_widget(self.peso_input)
        layout.add_widget(self.consumo_agua_input)
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
