import flet as ft

from services.exercicio_service import ExercicioService



def editar_exercicio(page, exercicio, voltar):


    nome = ft.TextField(

        label="Nome do exercício",

        value=exercicio.nome

    )



    peso = ft.TextField(

        label="Peso",

        value=str(exercicio.peso),

        keyboard_type=ft.KeyboardType.NUMBER

    )



    series = ft.TextField(

        label="Séries",

        value=str(exercicio.series),

        keyboard_type=ft.KeyboardType.NUMBER

    )



    repeticoes = ft.TextField(

        label="Repetições",

        value=str(exercicio.repeticoes),

        keyboard_type=ft.KeyboardType.NUMBER

    )




    def salvar(e):


        ExercicioService.editar(

            exercicio.id,

            nome.value,

            float(peso.value),

            int(series.value),

            int(repeticoes.value)

        )


        voltar()




    def retornar(e):

        voltar()




    page.clean()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=retornar

        ),



        ft.Text(

            "Editar Exercício",

            size=30,

            weight=ft.FontWeight.BOLD

        ),



        nome,

        peso,

        series,

        repeticoes,



        ft.FilledButton(

            content=ft.Text(

                "Salvar Alterações"

            ),

            on_click=salvar

        )

    )