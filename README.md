# calc_nicegui

### Description
This repository uses NiceGUI to create several apps.

---
### Architecture
Any architecture can be used, but the Model-View-Controller architecture lends itself well to NiceGUI.

---
### Tips
This is a collection of solutions that I have discovered while working with NiceGUI.
##### Update a Text Element
The easiest way to achieve this is using an html element that is updated by a button click.
```python
# Change html with button click
text = ui.html('I do not change', tag='em')

ui.button('change', on_click=lambda: text.set_content("I changed!"))
```
The important part of this example is the `set_content` method. This method can be called from a variety of locations including a response function to an api endpoint.

##### Setting up an API
FastAPI is used to create endpoints. Below are basic `GET` and `POST` examples. You can use a tool like [Postman](https://www.postman.com/) to test out the endpoints. Simply copy the url `http://localhost:8080` where NiceGUI is running and add the endpoint to the url. Then Postman will allow you to send various HTTP requests. THis is a great way to quickly test the API. Use `BaseModel` from the Python module `pydantic` to define the JSON data that is expected from a `POST` request. This will be the format of the JSON data that is sent to the app. Here is an example of a `POST` endpoint:
```python
stored_information = []

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# POST endpoint
@app.post("/store-info")
async def store_info(info: Item):
    stored_information.append(info)
    return {"message": "Info Stored!!!!"}
```
`GET` requests are simpler:
```python
# GET endpoint
@app.get("/get-info")
async def get_info():
    return {"stored_information": stored_information}
```
This request will return the contents of the list `stored_information` to the requester.

---
##### Uploading Documents
The `ui.upload()` component can be used to facilitate file uploading. The UI element looks like this before a file is uploaded:

![image](https://github.com/jmart5/calc_nicegui/assets/93228623/39bfdfe1-dc40-434f-80e5-da7c91f07c29)

Click the "plus" button for a file browser window to open. The user can select the file they want to update from there. Once a file is selected, the UI element looks like this: 

![image](https://github.com/jmart5/calc_nicegui/assets/93228623/c1d6228f-9c26-49b4-be03-23ee36c822a5)

Click the "cloud" button to upload the file. This action can be used to trigger functions. You can set it up to automatically upload the file using `auto_upload=True`.  For example: `ui.upload(on_upload=do_something, auto_upload=True).classes('max-w-full')`

**Ex. 1:** The following example shows how the function uses the `on_upload` attribute to trigger a function called `do_something`:
```python
# Triggers do_something() function. The UI only accepts .csv type files. 
ui.upload(on_upload=do_something).props('accept=.csv').classes('max-w-full')
```
**Ex. 2:** The next example uses a lambda function to trigger a notification. The uploaded file is represented by `e` and the name of the file can be retrieved as shown. 
```python
ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'))
```

**Ex. 3:** Save the uploaded file to the current working directory using `SpooledTemporaryFile`. The contents of the file are saved to the `new_file.csv` using the `open()` function.
```python
from nicegui import ui
import shutil
from tempfile import SpooledTemporaryFile

def do_something(e: events.UploadEventArguments):
    ui.notify(f'Uploaded {e.name}')

    with SpooledTemporaryFile() as spooled_file:
        e.content.seek(0)   # Move the pointer to the beginning of the file

        # Make a new file to save the content into
        with open("new_file.csv", "wb") as nf:
            shutil.copyfileobj(e.content, nf)


ui.upload(on_upload=do_something).props('accept=.csv').classes('max-w-full')
```
The `e` object is `<class 'nicegui.events.UploadEventArguments'>` while the content of `e.content` is of type `<class 'tempfile.SpooledTemporaryFile'>`. `tempfile.SpooledTemporaryFile` is a class provided by Python's tempfile module. It's a variant of tempfile. TemporaryFile provides the ability to use a temporary file residing in memory (RAM) until it reaches a certain size threshold, after which it's seamlessly moved to disk. 

The code in Example 3 creates a `spooled_file` object. The `shutil` and `tempfile` modules are required to perform this task. The `seek(0)` function is used to move the file pointer to the beginning of the file. This ensures that the file is read from the start. 

###    Async Function Example
```python
async def make_request():
    """make_request.

    Send an HTTP request to another process running on the same machine. Use async to allow this function to wait for a response. 
    """
    response = await run.io_bound(requests.post, "http://localhost:8080/start_something", timeout=3)
    ui.notify(response.status_code)
```

Ex. 4 Input Validation
The following example enforces rules defined using a regular expression and directly in the lambda function. It checks that the string starts with a letter of underscore. Any letter, number, or underscore can be used after the first character. The total length is limited to 40 characters.
```python
import re
from nicegui import ui

def is_valid_input(value):
    pattern = r'^[a-z_][a-z0-9_]{0,39}$'
    return re.match(pattern, value) is not None

ui.input(
    label='Text',
    placeholder='start typing',
    on_change=lambda e: result.set_text('you typed: ' + e.value),
    validation={
        'Input too long': lambda value: len(value) < 40,
        'Invalid characters': is_valid_input
    }
)
result = ui.label()
```

###    Assigning IDs to UI Elements Generated by Loops
This is a very common issue, and the creators of Nicegui wrote an excellent example on this [stackoverflow discussion](https://stackoverflow.com/questions/76726671/im-populating-some-cards-using-for-loop-in-nicegui-each-has-a-label-and-a-butto)

![image](https://github.com/jmart5/calc_nicegui/assets/93228623/dadbf509-dfb1-446d-8d4b-1d50db8246e5)

