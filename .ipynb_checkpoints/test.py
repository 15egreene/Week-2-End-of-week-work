def game_program():
    cart = []
    choice = ''
    while choice != 'quit':
        choice = input('What would you like to do?: Show/Add/Delete or Quit')
    if choice == 'show':
        print(f'This is your current cart! {cart}')
    elif choice == 'add':
        new_game = input('What would you like to add?')
        cart.append(new_game)
    elif choice == 'delete':
        new_game = input('What would you like to delete?')
        cart.remove(new_game)
    elif choice == 'quit':
        print(f'Thanks for shopping with us. Here is a receipt of your cart. {cart}')
    else:
        print('This is an invalid option')
        
game_program()