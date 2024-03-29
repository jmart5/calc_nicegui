#!/usr/bin/env python3
# This is based on the example "Slideshow" created by NiceGUI
from pathlib import Path

from nicegui import app, ui
from nicegui.events import KeyEventArguments

ui.query('.nicegui-content').classes('p-0')  # remove padding from the main content

folder = Path(__file__).parent / 'slides' 
files = sorted(f.name for f in folder.glob('*.png'))
index = 0


def handle_key(event: KeyEventArguments) -> None:
    global index
    if event.action.keydown:
        if event.key.arrow_right:
            index += 1
        if event.key.arrow_left:
            index -= 1
        index = index % len(files)
        slide.set_source(f'slides/{files[index]}')


app.add_static_files('/slides', folder)  # serve all files in this folder
slide = ui.image(f'slides/{files[index]}')  # show the first image
ui.keyboard(on_key=handle_key)  # handle keyboard events

ui.run()