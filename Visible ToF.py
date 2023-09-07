import flet as ft

def main(page: ft.page):
    # Define el color de la ventana
    page.window_bgcolor = ft.colors.BLUE_GREY
    page.bgcolor = ft.colors.BLUE_GREY
    # Campos de texto para nombre y apellido
    first_name = ft.TextField()
    last_name = ft.TextField()
    # Define si el widget será interactuable
    first_name.disabled = False
    last_name.disabled = False
    # Actualiza los widgets
    page.update()
    # Renderiza los widgets correspondientes
    page.add(first_name, last_name)

ft.app(target=main)