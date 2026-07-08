import flet as ft

from services.exercicio_service import ExercicioService



def detalhe_exercicio(page, exercicio):


    peso = ft.TextField(

        label="Novo peso",

        value=str(exercicio.peso)

    )


    def salvar(e):

        ExercicioService.aumentar_carga(

            exercicio.id,

            float(peso.value)

        )

        detalhe_exercicio(page, exercicio)



    def abrir_grafico(e):

        from pages.grafico import grafico


        grafico(

            page,

            exercicio

        )



    def voltar(e):

        from pages.treino import tela_treino


        page.clean()


        tela_treino(

            page,

            "",

            "",

            exercicio.treino_id

        )



    page.clean()


    page.add(


        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),


        ft.Text(

            exercicio.nome,

            size=30,

            weight=ft.FontWeight.BOLD

        ),


        ft.Text(

            f"Peso atual: {exercicio.peso} kg"

        ),


        peso,


        ft.FilledButton(

            "Atualizar carga",

            on_click=salvar

        ),


        ft.OutlinedButton(

            "📈 Gráfico",

            on_click=abrir_grafico

        )

    )