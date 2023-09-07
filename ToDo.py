import flet as ft

def main(page):

    def add_clicked(e):
        # Renderiza las casillas etiquetadas con el valor de la tarea
        page.add(ft.Checkbox(label=new_task.value))
        # Cada tarea se inicializa vacio
        new_task.value = ""
        # Se centra en el campo para agregar una nueva tarea
        new_task.focus()
        # Se actualizan los widgets
        new_task.update()

    # La variable de la tarea solicita un valor ingresado por el usuario
    # La pista es lo quieres que el usuario ingrese
    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # Se renderiza el arreglo con la barra de tarea y un boton
    # Al clickear en el boton llama la función y enviando los parametros
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

ft.app(target=main)