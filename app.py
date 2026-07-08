import flet as ft

from database import criar_banco, popular_banco
from pages.home import home



def main(page: ft.Page):


    criar_banco()

    popular_banco()



    page.title = "Treino+"



    # Tema claro
    page.theme_mode = ft.ThemeMode.LIGHT


    # Fundo geral
    page.bgcolor = ft.Colors.WHITE



    page.padding = 20


    page.scroll = ft.ScrollMode.AUTO



    page.window.width = 430

    page.window.height = 850



    page.add(

        home(page)

    )





ft.run(

    main,

    assets_dir="assets"

)