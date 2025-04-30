from datastructures.array import Array
from projects.project3.Drink import Drink
class Menu:
    def __init__(self):
        self._menu = []
        self._menu.append(Drink(name= 'Hot Cocoa', price= 4.00, size= 'Medium'))
        self._menu.append(Drink(name= 'Americano', price= 4.25, size= 'Medium'))
        self._menu.append(Drink(name= 'Latte', price= 5.00, size= 'Medium'))
        self._menu.append(Drink(name= 'Lemonade', price= 4.00, size= 'Medium'))
        self._menu.append(Drink(name= 'Iced Coffee', price= 3.50, size= 'Medium'))

    def get_drink(self, num: int) -> Drink:
        return self._menu[num]
    def print_name(self):
        for item in self._menu:
            print(item.name)
    def return_items(self) -> str:
        return self._menu
    def __str__(self):
        print(self._menu)



    
