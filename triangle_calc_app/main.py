from nicegui import ui

# Page General Information
ui.page_title('Triangle Calculator')

# Content
ui.label('Hello NiceGUI!')
ui.markdown('**Bold** not so bold!')

ui.separator()
ui.space()

# ui.input(label='Side A', placeholder='enter a number',
#          on_change=lambda e: result.set_text('you typed: ' + e.value),
#          validation={'Input too long': lambda value: len(value) < 20})
# result = ui.label()

#Side A Input
ui.input(label='Side A', placeholder='enter a number',
         on_change=lambda e: result.set_text(e.value),
         validation={'Input too long': lambda value: len(value) < 20})
result = ui.label()

# username = ui.input('username')
# label = ui.label().bind_text_from(username, 'value')
# i = ui.number(value=42).props('clearable')
# j = ui.number(value=33).props('clearable')
# ui.label().bind_text_from(i, 'value')
#ui.button('Calculate', on_click=lambda: ui.notify(result.text))
ui.button('Calculate', on_click=lambda: ui.notify(result.text))


###################
a = ui.input(label='Text', placeholder='start typing')
ui.button('Show A', on_click=lambda: ui.notify(a.value))

b = ui.input(label='Hi mom', placeholder='start typing')
ui.button('Show B', on_click=lambda: ui.notify(b.value))

temp = ui.label()
temp.set_text(b.value + a.value)
ui.button('Show C', on_click=lambda: ui.notify(temp.text))

ui.run()