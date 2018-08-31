inventory = {'gold': 100, 'torch': 6, 'rope': 2, 'dagger': 1, 'arrow': 15}

def print_inventory(stuff):
    item_total = 0
    print("Inventory:")

    for k, v in stuff.items():
        print(f"{v} {k}")
        item_total += v
    
    print(f"Total items in inventory: {item_total}")

print_inventory(inventory)