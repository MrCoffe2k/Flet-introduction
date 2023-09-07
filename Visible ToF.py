import flet as ft

def main(page: ft.page):
    page.window_bgcolor = ft.colors.BLUE_GREY
    page.bgcolor = ft.colors.BLUE_GREY
    first_name = ft.TextField()
    last_name = ft.TextField()
    first_name.disabled = False
    last_name.disabled = False
    page.update()
    page.add(first_name, last_name)

ft.app(target=main)