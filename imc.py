import flet as ft


def main(pagina: ft.Page):
    pagina.title = "Calculadora de IMC ⚖️"
    pagina.bgcolor = "#e3f2fd"
    pagina.horizontal_alignment = "center"

    titulo = ft.Text(
        value="CALCULADORA DE IMC",
        size=30,
        font_family="arial",
        color="#1565c0",
    )

    campo_peso = ft.TextField(label="Peso (kg)")
    campo_altura = ft.TextField(label="Altura (m)")
    campo_resultado = ft.Text(value="O seu resultado vai aparecer aqui!")

    def calcular_imc(e):
        peso = float(campo_peso.value)
        altura = float(campo_altura.value)

        imc = peso / (altura * altura)

        if imc < 18.5:
            nivel = "Abaixo do peso 🦴"
        elif imc < 25.0:
            nivel = "Peso ideal (Normal) ✅"
        elif imc < 30.0:
            nivel = "Sobrepeso ⚠️"
        else:
            nivel = "Obesidade 🚨"

        campo_resultado.value = f"Seu IMC é {imc:.2f} - Nível: {nivel}"
        pagina.update()

    botao_calcular = ft.ElevatedButton(
        content=ft.Text("CALCULAR IMC"), on_click=calcular_imc
    )

    pagina.controls = [
        titulo,
        campo_peso,
        campo_altura,
        botao_calcular,
        campo_resultado,
    ]

    pagina.update()


ft.run(main)