import flet as ft
from flet_route import Params,Basket

class SplashScreen:
    def __init__(self, page, src_icon:str, name_app:str, version_app:str):
        self.src_icon= src_icon
        self.name_app = name_app
        self.version_app = version_app
        self.page = page
        pass

    def view(self, page:ft.Page, params:Params, basket:Basket):

        return    ft.View("/splash_screen",[
            ft.Stack([
                ft.Container(
                    expand=True,
                    content=ft.Column([
                        ft.Image(src=self.src_icon, width=102, height=119),
                        ft.Text(self.name_app, size=40, weight=ft.FontWeight.NORMAL, color="Black", font_family="Saira_fonts")
                    ], expand=True, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0,),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text(f"Versão: {self.version_app}", color="Black", size=18, font_family="Saira_fonts"),
                    height=100,
                    bottom=0
                )
            ], alignment=ft.alignment.center, expand=True),
        ],bgcolor="White", padding=0)