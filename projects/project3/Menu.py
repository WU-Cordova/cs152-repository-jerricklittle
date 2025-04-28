from datastructures.array import Array
from projects.project3.Drink import Drink
class Menu:
    def __init__(self):
        self._menu = Array(starting_sequence= [], data_type= Drink)
        self._menu.append(Drink(name= 'Hot Cocoa', price= 4.00, size= 'Medium', description= 'Rich, creamy cocoa blended with steamed milk, topped with whipped cream.'))
        self._menu.append(Drink(name= 'Americano', price= 4.25, size= 'Medium', description= 'Bold espresso softened with hot water for a smooth, rich flavor.'))
        self._menu.append(Drink(name= 'Latte', price= 5.00, size= 'Medium', description= ' Smooth espresso blended with steamed milk for a creamy, mellow coffee experience.'))
        self._menu.append(Drink(name= 'Lemonade', price= 4.00, size= 'Medium', description= 'A crisp, refreshing blend of tart lemons and sweetened just right, served ice-cold.'))
        self._menu.append(Drink(name= 'Iced', price= 3.50, size= 'Medium', description= 'Chilled, bold coffee served over ice, with a splash of cream or milk for the perfect cool pick-me-up.'))

    def get_drink(self, num: int) -> Drink:
        return self._menu[num]

    def return_items(self) -> str:
        return self._menu
    def __str__(self):
        print(self._menu)



    
