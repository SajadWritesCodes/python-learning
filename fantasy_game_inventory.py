inventory = {
    'rope' : 1, 
    'gold coin' : 42, 
}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    
def display_inventory(inventory_list,total_items = 0):
    print('Inventory:')
    for item in inventory_list:
        print(inventory[item],item , sep= ' ')
        total_items += int(inventory[item])
    
    print('\n'*2,'Total number of items: ',total_items, sep='')
    
    return total_items

def add_to_inventory(inventory, added_items):
    for items in added_items:
        if items in inventory:
            inventory[items] += 1
        else:
            inventory[items] = '1'
    display_inventory(inventory)
    return inventory
            

def main():
    add_to_inventory(inventory, dragon_loot)

if __name__ == '__main__':
    main()