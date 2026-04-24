from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


def montar_trilha(consumo_agua: str) -> dict:
    consumo_base = {
        "baixo": 1.0,
        "medio": 1.5,
        "alto": 2.0,
    }
    consumo_diario = consumo_base.get(consumo_agua, 1.0)
    meta = 2.0
    dia_1 = consumo_diario
    dia_2 = min(consumo_diario + 0.5, 2.5)
    media = (dia_1 + dia_2) / 2

    return {
        "consumo_diario": consumo_diario,
        "meta": meta,
        "dia_1": dia_1,
        "dia_2": dia_2,
        "media": media,
    }


class AmagoApp(App):
    def build(self) -> BoxLayout:
        self.step = 0
        self.respostas = {}
        self.input_atual = None

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.renderizar_step()
        return self.layout

    def renderizar_step(self) -> None:
        self.layout.clear_widgets()
        self.input_atual = None

        titulo, conteudo, texto_botao = self.obter_conteudo_step()

        titulo_label = Label(
            text=titulo,
            font_size=24,
            bold=True,
            size_hint=(1, 0.18),
            halign="center",
            valign="middle",
        )
        titulo_label.bind(size=self._ajustar_label)

        conteudo_label = Label(
            text=conteudo,
            size_hint=(1, 0.45),
            halign="left",
            valign="middle",
        )
        conteudo_label.bind(size=self._ajustar_label)

        self.layout.add_widget(titulo_label)
        self.layout.add_widget(conteudo_label)

        if self.step in {1, 2, 3, 7, 8}:
            self.input_atual = TextInput(
                hint_text=self.obter_hint_step(),
                multiline=False,
                size_hint=(1, 0.15),
            )
            self.layout.add_widget(self.input_atual)

        botao = Button(text=texto_botao, size_hint=(1, 0.18))
        botao.bind(on_press=self.avancar_step)
        self.layout.add_widget(botao)

    def obter_conteudo_step(self) -> tuple[str, str, str]:
        conteudos = {
            0: (
                "Amago",
                "Bem-vindo a trilha guiada de hidratacao.\n"
                "Avance etapa por etapa para conhecer seu perfil e registrar sua pratica.",
                "Iniciar",
            ),
            1: ("Etapa 1", "Informe sua idade.", "Proximo"),
            2: ("Etapa 2", "Informe seu peso.", "Proximo"),
            3: (
                "Etapa 3",
                "Informe seu consumo de agua atual: baixo, medio ou alto.",
                "Proximo",
            ),
            4: (
                "Estudo 1",
                "A agua participa do equilibrio do corpo e ajuda no funcionamento diario.",
                "Continuar",
            ),
            5: (
                "Estudo 2",
                "Manter uma rotina de hidratacao reduz esquecimentos e facilita criar habito.",
                "Continuar",
            ),
            6: (
                "Estudo 3",
                "Sede, cansaco e boca seca podem indicar que voce precisa beber mais agua.",
                "Continuar",
            ),
            7: (
                "Exercicio",
                "Responda: voce costuma esquecer de beber agua? Digite sim ou nao.",
                "Proximo",
            ),
            8: (
                "Pratica",
                "Registre quanto voce bebeu hoje em litros.",
                "Proximo",
            ),
            9: (
                "Resultado final",
                "Resumo da trilha concluida.",
                "Finalizar",
            ),
        }
        return conteudos[self.step]

    def obter_hint_step(self) -> str:
        hints = {
            1: "Idade",
            2: "Peso",
            3: "Consumo de agua (baixo, medio, alto)",
            7: "sim ou nao",
            8: "Litros registrados hoje",
        }
        return hints[self.step]

    def avancar_step(self, _instance) -> None:
        if self.input_atual is not None:
            self.respostas[self.step] = self.input_atual.text.strip()

        if self.step < 9:
            self.step += 1
            self.renderizar_step()

    def _ajustar_label(self, label: Label, _size) -> None:
        label.text_size = label.size


if __name__ == "__main__":
    AmagoApp().run()
