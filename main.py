
shopping_list = [
    {
        "name": "Scouring pads",
        "quantity": 4,
        "purchased": True,
    },
    {
        "name": "Lawn edger string",
        "quantity": 1,
        "purchased": False,
    },
    {
        "name": "Shelf brackets",
        "quantity": 4,
        "purchased": False, 

    }

]

def display_item(item):
    print(f"Need to buy: {item["quantity"]} {item["name"]}")

    


def show_needed(items):
    for item in items:
        if item["purchased"] == False:
            display_item(item)
                

show_needed(shopping_list)
            

