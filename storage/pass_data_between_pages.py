"""pass_data_between_pages.py

Demonstrates how to use app.storage.user to
pass data between pages in the app.
"""
from nicegui import app, ui

@ui.page('/page2')
def page2():
    data = app.storage.user['color'] # loading the content saved to the key "color"
    ui.json_editor({'content': {'json': data}})

@ui.page('/page1')
def main():
    favorite_color = {}
    ui.input('name:').bind_value_to(favorite_color, 'name')

    def load_page2():
        #app.storage.user is a dictionary that stores user data.
        app.storage.user.update(color=favorite_color) #"color" is the new key name in the user dictionary. It can be any name.
        #The dictionary "favorite_color" is being saved as the value in the user storage. color:{favorite_color_dict}
        ui.navigate.to('page2') #This reroutes the user to the next page
    ui.button('submit', on_click=load_page2)

ui.run(storage_secret='secret')
