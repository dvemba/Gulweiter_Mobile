import flet as ft 
from flet_route import Params,Basket
from utils.AppBar import AppBar

class TableView:
    def __init__(self, page):
        self.page = page
        self.appbar = AppBar(self.page, 0, "Mesas")
        self.user_data = self.page.client_storage.get("token-Gulweiter")
        if not self.user_data:
            print(self.user_data)
            self.page.go('/login')
        pass
    
    def view(self, page:ft.Page, params:Params, basket:Basket):
        return ft.View('/tables', [
            self.appbar.build(),
            ft.Container(height=1, bgcolor="#E0E0E0"), 
            ft.Text("Tables")
        ], bgcolor='White', drawer=self.page.drawer)
        