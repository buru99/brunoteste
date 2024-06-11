import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.add(ft.TextField(label="Digite algo"))
ft.app(main)