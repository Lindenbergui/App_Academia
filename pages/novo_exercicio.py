import flet as ft

from services.exercicio_service import ExercicioService



def novo_exercicio(
    page,
    treino_id,
    grupo_id,
    grupo,
    treino_nome,
    descricao
):


    nome = ft.TextField(
        label="Nome do exercício"
    )


    peso = ft.TextField(
        label="Peso atual",
        value="0"
    )


    series = ft.TextField(
        label="Séries",
        value="4"
    )


    repeticoes = ft.TextField(
        label="Repetições",
        value="10"
    )



    def voltar(e):

        from pages.grupo import tela_grupo


        tela_grupo(

            page,

            grupo,

            treino_nome,

            descricao,

            treino_id

        )





    def salvar(e):


        ExercicioService.adicionar(

            treino_id,

            nome.value,

            float(peso.value),

            int(series.value),

            int(repeticoes.value),

            grupo_id

        )



        voltar(None)





    page.clean()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),



        ft.Text(

            f"Novo Exercício - {grupo.nome}",

            size=28,

            weight=ft.FontWeight.BOLD

        ),



        nome,


        peso,


        series,


        repeticoes,



        ft.FilledButton(

            content=ft.Text(

                "Salvar"

            ),

            on_click=salvar

        )

    )