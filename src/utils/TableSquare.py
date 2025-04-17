import flet as ft 

class TableSquare:
    def __init__(self):
        pass
    def build(self, table_num:int, color_table:str, type_table:str):
        return ft.Container(
            content=ft.Text(table_num, color='white', size=30),
            alignment=ft.alignment.center,
            width=100,
            height=100,
            bgcolor=color_table,
            border_radius=ft.border_radius.all(10)
        )