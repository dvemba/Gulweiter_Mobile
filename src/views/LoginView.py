import flet as ft
from flet_route import Params, Basket
from utils.Helpers import Helpers
from services.FirebaseAuth import FirebaseAuth

class LoginView:
    def __init__(self, page):
        self.page = page
        self.FirebaseAuth = FirebaseAuth()
        self.btn_ref = ft.Ref[ft.FilledButton]()
        self.input_email = ft.TextField(
                                label="E-MAIL", 
                                # border="underline", 
                                on_change=self.check_input,
        )
        self.input_password = ft.TextField(
                                    label="PASSWORD", 
                                    # border="underline", 
                                    password=True, 
                                    can_reveal_password=True,
                                    on_change=self.check_input
        )
        self.btn_entrar = ft.FilledButton(
            content=ft.Text("ENTRAR", color="White"), 
                bgcolor=Helpers().color_primary, 
                disabled=True, 
                opacity=0.2, 
                style=Helpers().button_style,
                expand=True,
                height=66,
                ref=self.btn_ref,
                on_click=lambda e:self.validate_login(e)
        )
        self.forgot_password = ft.TextButton(
            content=ft.Text("Esqueceu sua senha?", 
            style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE), size=20, color=Helpers().color_primary),
            style=ft.ButtonStyle(bgcolor=ft.Colors.TRANSPARENT))
        pass
    def view(self, page:ft.Page, params:Params, basket:Basket):
        return ft.View("/login",[
            ft.Stack([
                ft.Container(
                    content=ft.Text("LOGIN", size=35, weight="bold", opacity=0.3),
                    alignment=ft.alignment.center,
                    expand=True,
                    top=90
                ),
                ft.Container(
                    content=ft.Column([
                        self.input_email,
                        self.input_password,
                        ft.Container(
                            content= ft.Row([
                                self.btn_entrar
                            ],
                            expand=True
                        ),
                        height=66
                    ),
                    ft.Container(
                        content=self.forgot_password,
                        alignment=ft.alignment.center_left
                    )
                    ], alignment=ft.MainAxisAlignment.CENTER, 
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                                    expand=True, spacing=30),
                    expand=True,
                    margin=ft.margin.only(20, 0, 20, 0)
                )
                
            ], alignment=ft.alignment.center, expand=True)
        ], bgcolor="White", padding=0)
        
    def check_input(self, e):
        if (self.input_email.value != "" and self.input_password.value != ""):
            if (self.btn_ref.current):
                self.btn_ref.current.opacity  = 1.0
                self.btn_ref.current.disabled = False
                self.btn_ref.current.update()
        else:
            if (self.btn_ref.current):
                self.btn_ref.current.opacity  = 0.2
                self.btn_ref.current.disabled = True
                self.btn_ref.current.update()
        pass
    
    def validate_login(self, e):
        self.btn_ref.current.content = ft.ProgressRing(stroke_width=3, width=20, height=20, color='White')
        self.btn_ref.current.disabled = True
        self.btn_ref.current.update()
        user = self.FirebaseAuth.sign_in(self.input_email.value, self.input_password.value)
        self.btn_ref.current.content = ft.Text("ENTRAR", color="White")
        self.btn_ref.current.disabled = False
        self.btn_ref.current.update()
        if user:
            Helpers().snackbar(self.page, "Green","Login feito com sucesso!")
        else:
            Helpers().snackbar(self.page, "Red","Erro ao fazer o login.")
        pass