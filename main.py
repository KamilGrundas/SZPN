import flet as ft
from flet_app.views.home_view import home_view


def main(page: ft.Page):
    home_view(page)
    page.update()


ft.app(target=main, assets_dir="assets")
