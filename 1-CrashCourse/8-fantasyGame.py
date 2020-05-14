# Write a function named displayInventory() that would take 
# any possible “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

stuff = {"rope": 1, "dagger": 3, "torch": 2, "gold coin": 42}

def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        itemTotal += v
    print("Total number of items: " + str(itemTotal))
    return itemTotal

displayInventory(stuff)


