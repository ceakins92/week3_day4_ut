class cart():
    grocery_dict = {}
    """
        {
            grocery_item : {
                quantity: int,
                price: float
                }
        }
    
    
    """

    def driver(self):
        shopping = True
        while True:

            response = input(
                'Would you like to Add | Remove | Show | Quit ?\n').lower()

            if response == 'add':
                self.add()

            if response == 'remove':
                self.remove()

            if response == 'show':
                self.show()

            if response == 'quit':
                self.show()
                break

            else:
                print('Please choose from the list of options:\n')

    def add(self):
        item = input('What would you like to add?\n').lower()
        while True:
            quantity = input(f"How many {item} would you like to add?:\n")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print('Please enter quantity to ADD in digits')
        while True:
            try:
                price = float(input(f"How much does {item} cost?:\n"))
                break
            except:
                print('Please enter price in digits')
        if item in self.grocery_dict:
            pass
        else:
            self.grocery_dict[item] = {
                'quantity': quantity,
                'price': price
            }
        self.show()

    def remove(self):
        item_to_remove = input('What would you like to remove?\n').lower()
        while True:
            try:
                quantity = int(input('How many would you like to remove?\n'))
                break
            except:
                print('Please enter quantity in digits.')
        if item_to_remove in self.grocery_dict:
            self.grocery_dict[item_to_remove]['quantity'] -= quantity
            if self.grocery_dict[item_to_remove]['quantity'] < 1:
                self.grocery_dict.pop(item_to_remove)
        else:
            print("Item not in cart")
        self.show()

    def show(self):
        print(self.grocery_dict)


new_cart = cart()

new_cart.driver()
