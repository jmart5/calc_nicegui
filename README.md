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
