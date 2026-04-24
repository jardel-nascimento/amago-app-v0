from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


def montar_trilha(consumo_agua: str, registro_agua: float) -> dict:
    consumo_base = {
        "baixo": 1.0,
        "medio": 1.5,
        "alto": 2.0,
    }
    consumo_diario = consumo_base[consumo_agua]
    meta = 2.0
    diferenca_meta = registro_agua - meta

    return {
        "consumo_diario": consumo_diario,
        "meta": meta,
        "registro_agua": registro_agua,
        "diferenca_meta": diferenca_meta,
    }


class AmagoApp(App):
    def build(self) -> BoxLayout:
        self.step = 0
        self.respostas = {}
        self.input_atual = None
        self.mensagem_erro = ""

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

        if self.mensagem_erro:
            conteudo = f"{conteudo}\n\n{self.mensagem_erro}"

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
        if self.step == 9:
            return (
                "Resultado final",
                self.montar_resultado_final(),
                "Finalizar",
            )

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
        self.mensagem_erro = ""

        if self.input_atual is not None:
            try:
                self.salvar_resposta_atual()
            except ValueError as erro:
                self.mensagem_erro = str(erro)
                self.renderizar_step()
                return

        if self.step < 9:
            self.step += 1
            self.renderizar_step()

    def salvar_resposta_atual(self) -> None:
        valor = self.input_atual.text.strip()

        if not valor:
            raise ValueError("Preencha esta etapa para continuar.")

        if self.step == 1:
            self.respostas["idade"] = self.validar_idade(valor)
            return

        if self.step == 2:
            self.respostas["peso"] = self.validar_decimal_positivo(
                valor,
                "Peso deve ser numerico.",
            )
            return

        if self.step == 3:
            consumo_agua = valor.lower()
            if consumo_agua not in {"baixo", "medio", "alto"}:
                raise ValueError("Informe baixo, medio ou alto.")
            self.respostas["consumo_agua"] = consumo_agua
            return

        if self.step == 7:
            resposta = valor.lower()
            if resposta not in {"sim", "nao"}:
                raise ValueError("Digite sim ou nao.")
            self.respostas["esquece_agua"] = resposta
            return

        if self.step == 8:
            self.respostas["registro_agua"] = self.validar_decimal_positivo(
                valor,
                "Registro deve ser numerico.",
            )

    def validar_idade(self, valor: str) -> int:
        try:
            idade = int(valor)
        except ValueError as exc:
            raise ValueError("Idade deve ser um numero inteiro.") from exc

        if idade <= 0:
            raise ValueError("Idade deve ser maior que zero.")

        return idade

    def validar_decimal_positivo(self, valor: str, mensagem_erro: str) -> float:
        try:
            numero = float(valor.replace(",", "."))
        except ValueError as exc:
            raise ValueError(mensagem_erro) from exc

        if numero < 0:
            raise ValueError("Informe um valor maior ou igual a zero.")

        return numero

    def montar_resultado_final(self) -> str:
        trilha = montar_trilha(
            self.respostas["consumo_agua"],
            self.respostas["registro_agua"],
        )

        if trilha["diferenca_meta"] >= 0:
            status_meta = (
                f"Voce atingiu a meta com {trilha['diferenca_meta']:.1f} litros acima."
            )
        else:
            status_meta = (
                f"Faltaram {abs(trilha['diferenca_meta']):.1f} litros para a meta."
            )

        return (
            "Trilha de hidratacao concluida.\n\n"
            f"Idade: {self.respostas['idade']}\n"
            f"Peso: {self.respostas['peso']:.1f} kg\n"
            f"Consumo atual informado: {self.respostas['consumo_agua']}\n"
            f"Consumo diario estimado: {trilha['consumo_diario']:.1f} litros\n"
            f"Costuma esquecer de beber agua: {self.respostas['esquece_agua']}\n"
            f"Registro de hoje: {trilha['registro_agua']:.1f} litros\n"
            f"Meta da trilha: {trilha['meta']:.1f} litros\n"
            f"{status_meta}"
        )

    def _ajustar_label(self, label: Label, _size) -> None:
        label.text_size = label.size


if __name__ == "__main__":
    AmagoApp().run()
