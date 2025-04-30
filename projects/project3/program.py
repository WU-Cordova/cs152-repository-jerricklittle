from projects.project3.Menu import Menu
from projects.project3.Customer_Order import Customer_Order
from projects.project3.Order_Queue import Order_Queue
# from projects.project
def main():
    name = input('What is the name for the order?')
    customer_order = Customer_Order(name)
    order_queue = Order_Queue()
    order = customer_order.take_order()
    order_queue.add_order(order)
    print(order_queue.front_order())





if __name__ == '__main__':
    main()
