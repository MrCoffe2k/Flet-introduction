import flet as ft

def main(page):

    # Campos de texto de nombre y apellido enfocando en el nombre
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    # El saludo se almacena en una columna de datos
    greetings = ft.Column()

    # Función que controla que sucede al presionar el botón
    def btn_click(e):
        # Respuesta con las variables de nombre 
        # y apellidos almacenados
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        # Los valores de nombre y apellido se inicializan en vacio
        first_name.value = ""
        last_name.value = ""
        # Se actualiza el widget para agregarlo
        page.update()
        # Se enfoca en el nombre
        first_name.focus()

    # Se renderizan las variables de la aplicación junto con el botón
    page.add(
        first_name,
        last_name,
        # Botón con el texto que va a decir 
        # y llamando a la función de la presión del botón
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )

ft.app(target=main)