import flet as ft

from services.treino_service import TreinoService



def editar_treino(page, treino, voltar):


    nome = ft.TextField(

        label="Nome do treino",

        value=treino.nome

    )


    descricao = ft.TextField(

        label="Descrição",

        value=treino.descricao

    )



    def salvar(e):


        TreinoService.editar(

            treino.id,

            nome.value,

            descricao.value

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

            "✏️ Editar Treino",

            size=30,

            weight=ft.FontWeight.BOLD

        ),



        nome,



        descricao,



        ft.FilledButton(

            content=ft.Text(

                "Salvar Alterações"

            ),

            on_click=salvar

        )

    )