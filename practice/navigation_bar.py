from nicegui import ui

with ui.header().classes('items-center justify-between'):
    ui.avatar('favorite_border')
    with ui.row().classes('max-sm:hidden'):
        ui.button('Shop', icon='shopping_cart').props('flat color=white')
        ui.button('Blog', icon='feed').props('flat color=white')
        ui.button('Contact', icon='perm_phone_msg').props('flat color=white')
    with ui.row().classes('sm:hidden'):
        ui.button(icon='shopping_cart').props('flat color=white')
        ui.button(icon='feed').props('flat color=white')
        ui.button(icon='perm_phone_msg').props('flat color=white')
    ui.button(icon='menu').props('flat color=white')

ui.run()
