import flet as ft

from services.exercicio_service import ExercicioService
from components.exercicio_card import ExercicioCard
from pages.novo_exercicio import novo_exercicio



def tela_grupo(
    page,
    grupo,
    treino_nome,
    descricao,
    treino_id
):


    def registrar(exercicio):


        ExercicioService.registrar_treino(

            exercicio.id

        )


        tela_grupo(

            page,

            grupo,

            treino_nome,

            descricao,

            treino_id

        )





    def carregar_exercicios():


        cards = []


        exercicios = ExercicioService.listar(

            treino_id

        )


        for exercicio in exercicios:


            if hasattr(exercicio, "grupo_id"):


                if exercicio.grupo_id != grupo.id:

                    continue



            cards.append(


                ExercicioCard(

                    exercicio,


                    lambda e, ex=exercicio:

                        registrar(ex),



                    lambda e, ex=exercicio:

                        editar(ex),



                    lambda e, ex=exercicio:

                        excluir(ex),



                    lambda e, ex=exercicio:

                        abrir_grafico(ex)

                )

            )


        return cards





    def editar(exercicio):


        from pages.editar_exercicio import editar_exercicio


        editar_exercicio(

            page,

            exercicio,

            lambda:


                tela_grupo(

                    page,

                    grupo,

                    treino_nome,

                    descricao,

                    treino_id

                )

        )





    def excluir(exercicio):


        ExercicioService.excluir(

            exercicio.id

        )


        tela_grupo(

            page,

            grupo,

            treino_nome,

            descricao,

            treino_id

        )





    def abrir_grafico(exercicio):


        from pages.grafico import grafico


        grafico(

            page,

            exercicio

        )





    def criar_exercicio(e):


        novo_exercicio(

            page,

            treino_id,

            grupo.id,

            grupo,

            treino_nome,

            descricao

        )





    def voltar(e):


        from pages.treino import tela_treino


        tela_treino(

            page,

            treino_nome,

            descricao,

            treino_id

        )





    page.clean()



    exercicios = carregar_exercicios()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),



        ft.Text(

            grupo.nome,

            size=32,

            weight=ft.FontWeight.BOLD

        ),



        ft.Divider(),



        ft.Text(

            f"💪 Exercícios: {len(exercicios)}",

            size=20,

            weight=ft.FontWeight.BOLD

        ),



        *exercicios,



        ft.FilledButton(

            content=ft.Text(

                "➕ Novo Exercício"

            ),

            on_click=criar_exercicio

        )

    )