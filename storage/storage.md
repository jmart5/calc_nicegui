# Storage

User storage is a great way to store information that is unique to a user. This information is stored in a json file. The file for each user is created in a hidden directory inside the directory where the nicegui app is running. If the app is running in `/apps`, you can find these user storage files at `/apps/.nicegui/`.

### Updating User Storage
The underlying data structure for user storage is a dictionary. The following code demonstrates how to add a key-value pair to the users dictionary.
```pthon
def add_data():
    app.storage.user['new_data'] = "testing 1 2 3"

ui.button('add data', on_click=add_data)
```
This will add the key `new_data` to the user storage dictionary. Note - only the current user will have their user storage updated. Each user storage is unique to a user.

You can update values just like you would in any Python dictionary.
