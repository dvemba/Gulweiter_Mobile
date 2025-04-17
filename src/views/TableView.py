import flet as ft 
from flet_route import Params,Basket
from utils.AppBar import AppBar
from utils.Helpers import Helpers
from utils.TableSquare import TableSquare
import asyncio

class TableView:
    def __init__(self, page):
        self.page = page
        self.appbar = AppBar(self.page, 0, "Mesas")
        self.Container_ref = ft.Ref[ft.Container]()
        self.table_square = TableSquare()
        self.user_data = self.page.client_storage.get("token-Gulweiter")
        if not self.user_data:
            print(self.user_data)
            self.page.go('/login')
        pass
    
    def view(self, page:ft.Page, params:Params, basket:Basket):
        self.page.run_task(self.data)
        return ft.View('/tables', [
            self.appbar.build(),
            ft.Container(height=1, bgcolor="#E0E0E0"), 
            ft.Container(
                content=Helpers().loading(),
                ref=self.Container_ref,
                expand=True
            )
        ], bgcolor='White', drawer=self.page.drawer, padding=0)
    
    async def data(self):
        await asyncio.sleep(3)
        self.Container_ref.current.content = ft.GridView([
            self.table_square.build(1, "Blue", "Ocupado"),
            self.table_square.build(2, "Red", "Red"),
            self.table_square.build(3, "Blue", "Ocupado"),
            self.table_square.build(4, "Blue", "Ocupado"),
            self.table_square.build(5, "Grey", "Gray"),
            self.table_square.build(6, "Yellow", "Yellow")
        ],expand=1, cache_extent=3, runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,)
        self.Container_ref.current.margin = ft.margin.all(20)
        self.Container_ref.current.expand = False
        self.Container_ref.current.update()