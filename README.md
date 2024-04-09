# calc_nicegui

### Description
This repository uses NiceGUI to create several apps.

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

Click the "cloud" button to upload the file. This action can be used to trigger functions. The following example shows how the function uses the `on_upload` attribute to trigger a function called `do_something`:
```python
# Triggers do_something() function. The UI only accepts .csv type files. 
ui.upload(on_upload=do_something).props('accept=.csv').classes('max-w-full')
```
The next example uses a lambda function to trigger a notification. The uploaded file is represented by `e` and the name of the file can be retrieved as shown. 
```python
ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'))
```
