from methods import *

class Item:
    menu = {
        1  : {'name':'Filter Coffee', 'weight':2},
        2  : {'name':'Cappuccino',    'weight':3},
        3  : {'name':'Americano',     'weight':3},
        4  : {'name':'Latte',         'weight':4},
        5  : {'name':'Espresso',      'weight':4},
        6  : {'name':'Frappe',        'weight':5},
        7  : {'name':'Tea',           'weight':2},
        8  : {'name':'Fries',         'weight':3},
        9  : {'name':'Sandwich',      'weight':5},
        10 : {'name':'Chips',         'weight':1},
        11 : {'name':'Cookies',       'weight':1},
        12 : {'name':'Cake',          'weight':1}
    }

    def __init__(self, num):
        self.num    = num
        self.name   = self.menu[num]['name']
        self.weight = self.menu[num]['weight']

class Order(Item):
    def __init__(self, order_num, item_list, time_placed):
        self.order_num    = order_num
        self.order_list   = self.convert(item_list)
        self.status       = self.status()
        self.time_placed  = time_placed
        self.total_weight = self.get_total()
        self.num_items    = len(self.order_list)

    def status(flag):
        if flag == 0:
            return 'done'
        elif flag == 1:
            return 'wait'

    def convert(self, item_list):
        order_list = []

        for item_num in item_list:
            order_list.append(Item(item_num))

        return order_list

    def print_order(self):
        print(f"Order {self.order_num} ->", end=" ")

        for item in self.order_list[:-1]:
            print(f"{item.name}", end=", ")

        print(self.order_list[-1].name, end="\n")

    def get_total(self):
        total_weight = 0

        for item in self.order_list:
            total_weight = total_weight + item.weight

        return total_weight
        
    def return_order_list(self):
        return [item.name for item in self.order_list]

class Kitchen(Order):
    def __init__(self, pending, processing, fulfilled, pql):
        self.order_stack   = list(pending.queue)
        self.pending       = pending
        self.processing    = processing
        self.fulfilled     = fulfilled
        self.current_order = None

        self.total_load           = None#self.get_total_load()
        self.processing_queue_len = pql

    def add_order(self, order_num, item_list, time_placed):
        self.pending.put(Order(order_num, item_list, time_placed))

    def print_pending(self):
        print("\nPending orders:")

        for order in self.order_stack:
            order.print_order()

        print("\n")

    def process(self):
        # Shift orders from pending to processing:
        if self.pending.qsize()>0:
            while len(self.processing) < self.processing_queue_len:
                if self.pending.qsize()<=0:
                    break
                else:
                    self.processing.append(self.pending.get_nowait())
        
        # Sort procecssing list and shift lowest weighted order to fulfilled queue:
        if self.processing != []:
            self.processing.sort(key=lambda x: x.total_weight, reverse=True)
            self.current_order = self.processing.pop()
            self.fulfilled.put(self.current_order)

        # Subtract weight from all remaining orders in processing queue:
        for num in range(0,len(self.processing)):
            self.processing[num].total_weight = self.processing[num].total_weight - self.processing[num].num_items
