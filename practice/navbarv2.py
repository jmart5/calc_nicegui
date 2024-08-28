from nicegui import ui

ui.label("testing")

with ui.header().classes('items-center justify-between'):
    #ui.avatar('favorite_border')
    with ui.button(icon="menu"):
        with ui.menu() as menu:
            ui.menu_item("Home").classes("w-32")
            ui.menu_item("App 1").classes("w-32")
            ui.menu_item("App 2").classes("w-32")
            ui.menu_item("App 3").classes("w-32")


    with ui.row().classes('max-sm:hidden'):
        ui.label("My Applications")

    with ui.column():
        with ui.row().classes("w-full items-center"):
            ui.label("Welcome, Secret User")
            ui.button("Logout")

ui.run()
