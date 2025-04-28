from projects.project3.Menu import Menu
from projects.project3.Customer_Order import Customer_Order
# from projects.project
def main():
    menu = Menu.return_items()
    name = input('What is the name for the order?')
    customer_order = Customer_Order(name)
    more = 'Y'
    while  more.upper() == 'Y':
        start = input(f'What drink would you like today? {print(menu)}')
        if start == 1:
            customer_order.add_drink(menu.get_drink(0))
        elif start == 2:
            customer_order.add_drink(menu.get_drink(1))
        elif start == 3:
            customer_order.add_drink(menu.get_drink(2))
        elif start == 4:
            customer_order.add_drink(menu.get_drink(3))
        elif start == 5:
            customer_order.add_drink(menu.get_drink(4))
        more = input('Would you like to order another? (Y)es or (N)o')
    customer_order.repeat_order()






if __name__ == '__main__':
    main()
