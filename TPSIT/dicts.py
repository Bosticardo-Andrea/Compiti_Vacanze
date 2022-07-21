def create_inventory(items):
    inventario = {}
    add_items(inventario, items)
    return inventario
def add_items(inventory, items):
    for i in items:inventory[i] = inventory.get(i, 0) + 1
    return inventory
def decrement_items(inventory, items):
    for i in items:
        if inventory[i] > 0: inventory[i] -= 1
    return inventory
def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory
def list_inventory(inventory):
    output = [(k, v) for k, v in inventory.items() if inventory[k] > 0]
    return output
