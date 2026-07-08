import flet as ft

from database import buscar_usuario, salvar_usuario



def perfil(page: ft.Page):


    nome_atual = buscar_usuario()



    campo_nome = ft.TextField(

        label="Seu nome",

        value=nome_atual,

        width=300

    )





    def salvar(e):


        salvar_usuario(

            campo_nome.value

        )


        voltar(None)






    def voltar(e):


        from pages.home import home


        page.clean()


        page.add(

            home(page)

        )





    page.clean()



    page.add(



        ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=voltar

        ),




        ft.Text(

            "👤 Perfil",

            size=32,

            weight=ft.FontWeight.BOLD

        ),




        ft.Text(

            "Configure seu nome",

            size=18

        ),




        campo_nome,





        ft.FilledButton(

            content=ft.Text(

                "Salvar"

            ),

            on_click=salvar

        )

    )