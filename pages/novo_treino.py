import flet as ft

from services.treino_service import TreinoService



def novo_treino(page):


    nome = ft.TextField(

        label="Nome do treino",

        hint_text="Ex: Treino D"

    )


    descricao = ft.TextField(

        label="Descrição",

        hint_text="Ex: Ombro e Abdômen"

    )



    def voltar(e):

        from pages.home import home


        page.clean()


        page.add(

            home(page)

        )




    def salvar(e):


        TreinoService.adicionar(

            nome.value,

            descricao.value

        )


        voltar(None)




    page.clean()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),



        ft.Text(

            "➕ Novo Treino",

            size=30,

            weight=ft.FontWeight.BOLD

        ),



        nome,



        descricao,



        ft.FilledButton(

            content=ft.Text(

                "Salvar Treino"

            ),

            on_click=salvar

        )

    )