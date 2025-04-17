import flet as ft 
from flet_route import Params,Basket
from utils.AppBar import AppBar
from utils.Helpers import Helpers
from utils.TableSquare import TableSquare
import asyncio

class TableView:
    def __init__(self, page, FirestoreService):
        self.page = page
        self.FirestoreService = FirestoreService
        self.appbar = AppBar(self.page, 0, "Mesas")
        self.Container_ref = ft.Ref[ft.Container]()
        self.table_square = TableSquare()
        self.Token = self.page.client_storage.get("token-Gulweiter")
        self.user_data = None
        if not self.Token:
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
        ], bgcolor='White', drawer=self.page.drawer, padding=0, scroll=ft.ScrollMode.AUTO)
    
    async def data(self):
        await asyncio.sleep(0.0000001)
        self.user_data = self.FirestoreService.get_document('Users', self.Token['UserId'])
        print("id:::::",self.user_data['Restaurant_id'])
        table_data = self.FirestoreService.query_collection('Tables',"Restaurant_id", "==", self.user_data['Restaurant_id'])
        print(table_data)
        
        list_table = ft.GridView(
            expand=1, cache_extent=3, runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=10,)
        
        for data in table_data:
            list_table.controls.append(self.table_square.build(data['data']['Number'],data['data']['Status']))
            pass
        self.Container_ref.current.content = list_table
        # self.Container_ref.current.content = ft.GridView([
        #     self.table_square.build(1, "Blue", "Ocupado"),
        #     self.table_square.build(2, "Red", "Red"),
        #     self.table_square.build(3, "Blue", "Ocupado"),
        #     self.table_square.build(4, "Blue", "Ocupado"),
        #     self.table_square.build(5, "Grey", "Gray"),
        #     self.table_square.build(6, "Yellow", "Yellow")
        # ],expand=1, cache_extent=3, runs_count=5,
        # max_extent=150,
        # child_aspect_ratio=1.0,
        # spacing=10,
        # run_spacing=10,)
        self.Container_ref.current.margin = ft.margin.all(20)
        self.Container_ref.current.expand = False
        self.Container_ref.current.update()
        