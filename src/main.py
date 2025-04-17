import flet as ft
from flet_route import Routing, path, ViewNotFound, Basket, Params
from views.SplashScreen import SplashScreen
from views.LoginView import LoginView
from views.TableView import TableView
from services.FirestoreService import FirestoreService
import time

def home(page:ft.Page, params:Params, basket:Basket):
    return ft.View("/",[
        ft.Text("Hello Home!")
    ])
Firestore = FirestoreService()

def main(page: ft.Page):
    page.padding = 0
    page.fonts = {
        "Saira_fonts": "fonts/Saira-Medium.ttf" 
    } 
    theme = ft.Theme()
    theme.page_transitions = ft.PageTransitionsTheme(android=ft.PageTransitionTheme.NONE, ios=ft.PageTransitionTheme.NONE)
    page.theme = theme
    page.theme_mode = "Light"

    # page.client_storage.remove("token-Gulweiter")
    page.add(SplashScreen("https://www.dropbox.com/scl/fi/cvb1o5ww79uonl6bhwvs4/logo.png?rlkey=qjm79z9vob8pgdgnifslozb9a&st=g2rpyr5t&dl=1", "Gulweiter", "0.1.0").view())
    time.sleep(5)
    page.route = '/tables'
    app_routes = [
        path("/login",True, LoginView(page).view),
        path("/tables", True, TableView(page, Firestore).view)
    ]
    Routing(page,app_routes,not_found_view=ViewNotFound)
    page.go(page.route) 

ft.app(main, assets_dir="assets") 