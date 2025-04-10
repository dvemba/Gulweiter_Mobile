import flet as ft
from flet_route import Routing, path, ViewNotFound, Basket, Params
from views.SplashScreen import SplashScreen

def main(page: ft.Page):

    page.fonts = {
        "Saira_fonts": "fonts/Saira-Medium.ttf"
    }
    theme = ft.Theme()
    theme.page_transitions = ft.PageTransitionsTheme(android=ft.PageTransitionTheme.NONE, ios=ft.PageTransitionTheme.NONE)
    page.theme = theme
    page.theme_mode = "Light"

    page.route = "/splash_screen"
    app_routes = [
        path("/splash_screen",True, SplashScreen("https://www.dropbox.com/scl/fi/cvb1o5ww79uonl6bhwvs4/logo.png?rlkey=qjm79z9vob8pgdgnifslozb9a&st=g2rpyr5t&dl=1","Gulweiter","0.1.0").view),
    ]

    Routing(page,app_routes,not_found_view=ViewNotFound)
    page.go(page.route)

ft.app(main, assets_dir="assets")