from datastructures.deque import Deque
from datastructures.liststack import ListStack
from projects.project3.Customer_Order import Customer_Order

class Order_Queue:
    def __init__(self):
        self.queue = Deque(data_type= Customer_Order)
        self._complete_queue = ListStack(data_type= Customer_Order)
        
    def add_order(self, customer_order: Customer_Order) -> None:  
        self.queue.enqueue(customer_order)
        

    def front_order(self) -> Customer_Order:
        return self.queue.front()
    
    def complete_order(self) -> None:  
        done = self.queue.dequeue()
        self._complete_queue.push(done)
        sum = 0
        while not self._complete_queue.empty:
            completed_order = self._complete_queue.pop()
            sum += completed_order.total_price()
        return sum
        



    