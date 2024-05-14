"""dynamic_ui.py

Demonstrates dynamically generating UI elements
using a for loop. This example also highlights
a method for linking the button UI with the content
displayed on each line. This was achieved by defining
the current index element from the list as it is
created in each row. It is critical to 'save' this value
in the lambda of each button, because this binds the
index value at the time of the create to the button in 
that same row.
"""
from nicegui import ui

fruits = ['apples', 'banana', 'grape', 'berry', 'orange']

index = 0
for fruit in fruits:
    with ui.row().style("margin-top: 10px"):
        ui.label(fruit)
        ui.button("Run", on_click=lambda current_index = index: ui.notify(f'Hello, {fruits[current_index]}'))
    index += 1

ui.run()
