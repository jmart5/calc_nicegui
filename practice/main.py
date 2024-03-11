from nicegui import ui
import pandas as pd
import random

ui.page_title("NiceGUI Practice")

# Text
ui.label("This is a label")
# Markdown
ui.markdown("### This is a markdown")
# HTML
ui.html("<p>This is a paragraph tag</p>")
# Mermaid
ui.mermaid("""
           graph TD;
           A-->B;
           A-->C;
           B-->D;
           D-->E;
           C-->E;
           """)

###### Inputs(A.K.A. Widgets) #####
# Text Input
ui.input(label="Firstname", on_change= lambda e: fname.set_text(e.value))
fname = ui.label()  #This label is binded to the input value in the line above
# Text Area
ui.textarea(label="A Message", on_change=lambda e: msg.set_text(e.value))
msg = ui.label()    #Binded to the textarea above.

# Number
ui.number(label="Age", min=2, max=100)

# Date
ui.date(value="2024-03-11")

# Time
ui.time(value="12:00")

# Color
ui.color_input()
# Color Picker: ui.color_picker()

# Button
ui.button(text="Click Me", on_click=lambda e: ui.notify("You clicked me"))
# Radio Button
radio1 = ui.radio([1,2,5],value=2).props("inline")  #By default, value 2 is selected
# Select (Drop-Down Menu)
select_gender = ui.select(["M", "F", "Prefer Not To Say"])
# Check Box
checkbox = ui.checkbox("Append")
# Switch
switch_btn = ui.switch("This is a Switch")
# Slider
slider_value = ui.label()
slider = ui.slider(min=100, max=20000, value=5000, on_change=lambda e: slider_value.set_text(e.value))

##### Media #####
# Image
ui.image(source="a.PNG").props('fit=scale-down')
# ui.audio()
# ui.video()

# Data and Table (import pandas as pd)
df = pd.read_csv("fruits.csv")
ui.aggrid.from_pandas(df)

# Code
ui.code("""
# This is code being placed on the webpage similar to how markdown files do it
print("Hello, World!")
        """)

ui.code("""
// This is code being placed on the webpage similar to how markdown files do it (Java Example)
class Test
{
    public static void main(String []args)
    {
        System.out.println("My First Java Program.");
    }
};
        """, language="java")

# Message and Chat Elements
ui.chat_message("hello this is fun!")

# Separator
ui.separator()

# Pages
@ui.page("/blog")
def blog():
    ui.label("This is a blog page")

ui.link("Blog", blog)

# Card
with ui.card().tight():
    ui.image(source="a.PNG")
    with ui.card_section():
        ui.label("This is a card")
    with ui.card_actions():
        ui.button("button here")

# File Upload
ui.upload(label="Upload txt")
# File Download
#ui.download(src="fruits.csv")

# Dark Mode
dark = ui.dark_mode()
ui.button("Dark Mode", on_click=dark.enable)
ui.button("Light Mode", on_click=dark.disable)

##### Binding #####
class Todo:
    def __init__(self) -> None:
        self.number = 1
        self.task = ""

todo = Todo()
ui.input("task").bind_value(todo, "task")
ui.label().bind_text(todo, "task")  # Show


##### Math Test #####
# Dictionary that stores values from inputs
data = {"numbers": [1,2], "temp_number": "", "x": 0, "y": 0, "z": 0, 'sum': None}

# Inputs
x = ui.input("X: Enter a number here")
y = ui.input("Y: Enter a number ")
z = ui.input("Z: Enter another number")

@ui.refreshable
def number_ui() -> None:
    ui.label(', '.join(str(n) for n in sorted(data['numbers'])))

def add_number() -> None:
    data['numbers'].append(int(x.value))
    #numbers.append(random.randint(0, 100))
    number_ui.refresh()

def get_number_from_input() -> None:
    temp_number = int(x.value)

def sum_xyz() -> None:
    #Save the user input values
    data['x'] = int(x.value)
    data['y'] = int(y.value)
    data['z'] = int(z.value)

    #Perform calculation and notification 
    ans = int(data['x']) +int(data['y'])  + int(data['z'])
    ui.notify(ans)

# Create a function to run multiple functions (use this in the on_click trigger)
def multiFunction() -> None:
    add_number()
    #get_number_from_input()
    ui.notify(data['numbers'])

ui.button(text="Solve", on_click=lambda e: multiFunction())
ui.button(text="Get Sum of X Y Z", on_click=sum_xyz)

ui.run()
