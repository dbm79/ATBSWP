inventory = {'gold': 100, 'torch': 6, 'rope': 2, 'dagger': 1, 'arrow': 15}
dragon_loot = ['gold', 'ruby', 'shield', 'gold', 'dagger', 'gold']

def print_inventory(stuff):
    item_total = 0
    print("Inventory:")

    for k, v in stuff.items():
        print(f"{v} {k}")
        item_total += v
    
    print(f"Total items in inventory: {item_total}")

def add_inventory(stuff, loot):
    for item in loot:
        if item in stuff.keys():
            stuff[item] += 1
        else:
            stuff.setdefault(item, 1)
    return stuff

print_inventory(inventory)
inventory = add_inventory(inventory, dragon_loot)
print_inventory(inventory)