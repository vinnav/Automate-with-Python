def displayInventory(inventory):
    itemTotal = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + " " + k)
        itemTotal += v
    print("Total number of items: " + str(itemTotal))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)


