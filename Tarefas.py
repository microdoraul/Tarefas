import flet as ft

def main(pagina: ft.Page):
    # Configurações visuais da janela principal
    pagina.title = "Analisador de Tarefas"
    pagina.bgcolor = "#e3f2fd"
    pagina.horizontal_alignment = "center"

    # Título grande no topo da tela
    titulo = ft.Text(
        value="Analisador de Tarefas",
        size=30,
        font_family="Arial",
        color="#1565c0",
    )

    # Caixa de texto onde você digita
    campo_analisador = ft.TextField(
        label="Digite sua tarefa",
        bgcolor="#9691f2",
        border_radius=30,
        border_color="#000000",
        expand=True
    )

    co

    # Coluna visual que vai guardar os textos das tarefas na tela
    lista_visual = ft.Column()

    # Função que é chamada ao clicar no botão
    def adicionar_tarefa(e):
        if campo_analisador.value:
            # Adiciona o texto digitado como um novo Text dentro da coluna visual
            lista_visual.controls.append(ft.Text(value=campo_analisador.value, size=18))
            campo_analisador.value = ""  # Limpa o campo
            pagina.update()  # Atualiza a tela

    # Botão de incluir
    botao_analisar = ft.ElevatedButton(
        content=ft.Text("INCLUIR"), 
        on_click=adicionar_tarefa
    )

    # Linha que junta a caixa de texto e o botão lado a lado
    linha_entrada = ft.Row(controls=[campo_analisador, botao_analisar])

    # Elementos que vão aparecer na tela
    pagina.controls = [
        titulo,
        linha_entrada,
        lista_visual
    ]

    pagina.update()

ft.run(main)