import flet as ft
from utils.Helpers import Helpers 

class AppBar:
    def __init__(self, page, index_bar:int ,title,):
        self.title = title
        self.page = page
        self.index_bar = index_bar
        self.page.drawer = ft.NavigationDrawer([
            ft.NavigationDrawerDestination("Mesas", icon=ft.Icon(ft.Icons.TABLE_BAR),bgcolor='White'),
            ft.NavigationDrawerDestination("Reservar Mesas", icon = ft.Icon(ft.Icons.ACCESS_TIME_ROUNDED)),
            ft.NavigationDrawerDestination("Configuracao", icon=ft.Icon(ft.Icons.SETTINGS_ROUNDED)),
            ft.Divider(thickness=2),
        ], bgcolor='White', 
            indicator_color=Helpers().color_primary, 
            selected_index=self.index_bar,
        )
        pass
    
    def build(self):
        return ft.AppBar(
            leading=ft.IconButton(ft.Icons.MENU_ROUNDED, icon_color="Black", icon_size=32, on_click=lambda e:self.navigation_drawer(e)),
            title=ft.Text(self.title, color='Black'),
            bgcolor="White",
            
        )
        
    def navigation_drawer(self, e):
        if not self.page.drawer.open:
            self.page.drawer.open = True
            self.page.update()