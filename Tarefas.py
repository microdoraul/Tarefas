import flet as ft

def main (pagina: ft.Page):
    pagina.title= "Analisador de Tarefas"
    pagina.bgcolor= "#e3f2fd"
    pagina.horizontal_alignment = "center"


    titulo = ft.Text(
        value="Analisador de Tarefas",
        size=30,
        font_family="Arial",
        color= "#1565c0",
)
    campo_analisador= ft.TextField(label="Analisador",
                                   bgcolor="#9691f2",
                                   border_radius=30,
                                   border_color="#0000000,")
    botao_analisar= ft.ElevatedButton(
        content=ft.Text("Analisador de Tarefas"), on_click=campo_analisador
    )


    pagina.controls =[
    titulo,
    campo_analisador,
    botao_analisar,
    ]

    pagina.update()

ft.run(main)