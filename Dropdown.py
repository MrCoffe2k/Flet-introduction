import flet as ft

def main(page: ft.Page):

    # Función que define que comportamiento 
    # y que opciones tendra el dropdown
    def button_clicked(e):
        # Responde con el valor que se seleccionó en el dropdown tomando la variable correspondiente
        output_text.value = f"Dropdown value is:    {color_dropdown.value}"
        # Actualiza la aplicación
        page.update()

    # Define los widgets que se estarán utilizando
    output_text = ft.Text()
    # Botón que llama a la función del botón al clickearse
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    # Opciones que serán seleccionables en el dropdown
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    # Renderiza los widgets
    page.add(color_dropdown, submit_btn, output_text)
    
ft.app(target=main)