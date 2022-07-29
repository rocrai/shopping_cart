print()
print('Welcome to the Shopping Cart Program!')
print()
action = 0
items = []
prices = []
while action < 5:
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = int(input('Please enter an action: '))
    print()
    if action == 1:
        items_add = input('What item would you like to add? ')
        items.append(items_add)
        price_add = float(input(f'What is the price of \'{items_add}\'? '))
        prices.append(price_add)
        howmany = int(input(f'How many \'{items_add}\' would you like to purchase? '))
        quantity = 1
        while howmany != quantity:
            items.append(items_add)
            prices.append(price_add)
            quantity = quantity + 1
        print(f'\'{items_add}\' has been added to the cart.')
        print()
                
    elif action == 2:
        print('The contents of the shopping cart are:')
        for i in range(len(items)):
            print(f'{i +1}. {items[i]} - ${prices[i]:.2f}')
        print()
    elif action == 3:
        item_remove = 0
        if (len(items)) > item_remove:
            item_remove = int(input('Which item would you like to remove? '))
            if item_remove > (len(items)) + 1:
                print('Sorry, that is not a valid item number')
                print()
            else:   
                item_remove1 = item_remove - 1
                items.pop(item_remove1)
                prices.pop(item_remove1)
                print('Item removed.')
                print()
    elif action == 4:
        totalprice = 0
        average = 0
        for i in range(len(prices)):
            totalprice += prices[i]
            
        print(f'The total price of the items in the shopping cart is ${totalprice:.2f}')
        print()
    else:
        break
print('Thank you. Goodbye.')

#5. I added a function to let the user choose how much quantity they would like to purchase.