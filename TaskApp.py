import flet as ft

def main(page: ft.Page):
    text = ft.Text(value="Este es un texto de ejemplo", color= "blue", size= "25")
    page.controls.append(text)
    page.update()
    pass
ft.app(target=main)