import flet as ft 

class Helpers:
    def __init__(self):
        self.color_primary = "#111111"
        self.color_white = "#FFFFFF"
        self.button_style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    def snackbar(self, page, Color, Info):
        snack_bar = ft.SnackBar(
            ft.Text(Info, color='White'),
            open=True, bgcolor=Color, 
            behavior=ft.SnackBarBehavior.FLOATING, dismiss_direction=ft.DismissDirection.UP, 
            close_icon_color='White', duration=2000,
            
        )
        page.overlay.append(snack_bar) 
        page.update()