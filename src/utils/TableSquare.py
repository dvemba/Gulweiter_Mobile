import flet as ft 

class TableSquare:
    def __init__(self):
        self.color = {
            "Ocupado": "#44B6D0",
            "Livre": "#C9C9C9",
            "Reservado": "#ebd13d",
            "Conta_fechada": " Red"
        }
        pass
    def build(self, table_num:int, type_table:str):
        color = None
        if type_table == 'Ocupado':
            color = self.color['Ocupado']
        elif type_table == 'Livre':
            color = self.color['Livre']
        elif type_table == 'Reservado':
            color = self.color['Reservado']
        elif type_table == 'Conta_fechada':
            color = self.color['Conta_fechada']
        return ft.Container(
            content=ft.Text(table_num, color='white', size=30),
            alignment=ft.alignment.center,
            width=100,
            height=100,
            bgcolor=color,
            border_radius=ft.border_radius.all(10)
        )