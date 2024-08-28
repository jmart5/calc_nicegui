#  Practice

### dynamic_ui.py
This example demonstrates how to dynamically generate multiple occurences of UI elements based on the inputs provided. In this situation, a list is used, but this could be a list of objects or other more complex items.

![image](https://github.com/jmart5/calc_nicegui/assets/93228623/4be9b781-c752-445e-a8ab-552361fabb3f)

As you can see in the image above, each button corresponds to the label created on the same row. It is important to ensure that these two items are linked somehow. This was achieved by capturing the list index value during each iteration of the for loop. The current value of the index is saved at the time of creation of the index value. When the button is clicked, it will use this saved index value. This is critical, as this value corresponds with the item created on the same row. 

Without this step, the lambda function would use the incorrect index value. If you did not define the index value at the time of creation of the button, all lambda functions (each button created) will reference the final value of the index (the value of index at the end of the for loop).

![image](https://github.com/jmart5/calc_nicegui/assets/93228623/ee89d673-6fe6-4fd9-9b40-c7674bc52dba)

The image above shows that the button created on the same row as the `berry` label succesfully referenced the index of the fruits list corresponding to `berry`.

### Navigation Bar Spacing
The spacing of items in the navigation bar can be difficult. The code in `navbarv2` produced the following well spaced navbar:

![image](https://github.com/user-attachments/assets/66ca2c08-a20c-48f8-85f2-a9480c3f0132)
