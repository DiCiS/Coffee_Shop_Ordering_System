from classes import *
from queue import Queue
import datetime, time, sys, os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def processing_anim(wait_time, order_num):
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(wait_time)
        sys.stdout.write("\r" + "Processing Order: " + animation[i % len(animation)])
        sys.stdout.flush()

    print(f"\nOrder {order_num} Fulfilled!!")
    print()

def display_menu(kitchen):
    print("--------MENU--------")
    print("\nCoffee:")
    print(f"Filter Coffee [W={kitchen.menu[1]['weight']}]  -> 1")
    print(f"Cappuccino    [W={kitchen.menu[2]['weight']}]  -> 2")
    print(f"Americano     [W={kitchen.menu[3]['weight']}]  -> 3")
    print(f"Latte         [W={kitchen.menu[4]['weight']}]  -> 4")
    print(f"Espresso      [W={kitchen.menu[5]['weight']}]  -> 5")
    print(f"Frappe        [W={kitchen.menu[6]['weight']}]  -> 6")
    print("--------------------")
    print("\nAppetizers:")
    print(f"Tea           [W={kitchen.menu[7]['weight']}]  -> 7")
    print(f"Fries         [W={kitchen.menu[8]['weight']}]  -> 8")
    print(f"Sandwich      [W={kitchen.menu[9]['weight']}]  -> 9")
    print("--------------------")
    print("\nSnacks:")
    print(f"Chips         [W={kitchen.menu[10]['weight']}] -> 10")
    print(f"Cookies       [W={kitchen.menu[11]['weight']}] -> 11")
    print(f"Cake          [W={kitchen.menu[12]['weight']}] -> 12")
    print("--------------------")

def place_order():
    s1 = "Place order (Enter item num separated by space): "

    ord_str = input(s1)

    return [int(x) for x in ord_str.split()]

def initialize_data_structures(initial_pending_queue):
    pending_queue   = Queue(maxsize=0)
    fulfilled_queue = Queue(maxsize=0)
    processing_list = []

    if initial_pending_queue == []:
        return (pending_queue, processing_list, fulfilled_queue)
    else:
        for item in initial_pending_queue:
            pending_queue.put(item)
        
        return (pending_queue, processing_list, fulfilled_queue)

def get_time():
    curr_time = datetime.datetime.now()

    return curr_time.strftime("%I:%M:%S %p")

def print_weights(Kitchen):
    pending    = list(Kitchen.pending.queue)
    processing = Kitchen.processing
    fulfilled  = list(Kitchen.fulfilled.queue)

    print()

    # pending:
    print("Pending:    ", end="")
    if pending != []:
        print(f"[{pending[0].total_weight}", end="")    
        for order in pending[1:]:
            print(f"<-{order.total_weight}", end="")

        print("]", end="\n")
    else:
        print("[*empty*]")

    # processing:
    print("Processing:  ", end="")
    if processing != []:
        print(f"[{processing[0].total_weight}", end="")    
        for order in processing[1:]:
            print(f"->{order.total_weight}", end="")

        print("]", end="\n")
    else:
        print("[*empty*]")

    # fulfilled:
    print("Fulfilled:  ", end="")
    if fulfilled != []:
        print(f"[{fulfilled[0].total_weight}", end="")    
        for order in fulfilled[1:]:
            print(f"<-{order.total_weight}", end="")

        print("]", end="\n")
    else:
        print("[*empty*]")

    print("\n")

def print_orders(Kitchen):
    pending    = list(Kitchen.pending.queue)
    processing = Kitchen.processing
    fulfilled  = list(Kitchen.fulfilled.queue)

    print()

    # pending:
    print("Pending:    ", end="")
    if pending != []:
        print(f"[{pending[0].order_num}", end="")    
        for order in pending[1:]:
            print(f"<-{order.order_num}", end="")

        print("]", end="\n")
    else:
        print("[*empty*]")

    # processing:
    print("Processing: ", end="")
    if processing != []:
        print(f"[{processing[0].order_num}", end="")    
        for order in processing[1:]:
            print(f"->{order.order_num}", end="")

        print("->X]", end="\n")
    else:
        print("[*empty*]")

    # fulfilled:
    print("Fulfilled:  ", end="")
    if fulfilled != []:
        print(f"[{fulfilled[0].order_num}", end="")    
        for order in fulfilled[1:]:
            print(f"<-{order.order_num}", end="")

        print("]", end="\n")
    else:
        print("[*empty*]")

    print("\n")

def print_ord_wgt(list_name, ord_list, type='ord'):
    if type == 'ord':
        print(f"{list_name}", end="")
        if ord_list != []:
            print(f"[{ord_list[0].order_num}", end="")
            for order in ord_list[1:]:
                print(f"<-{order.order_num}", end="")

            print("]", end="\n")
        else:
            print("[*empty*]")

    if type == 'wgt':
        print(f"{list_name}", end="")
        if ord_list != []:
            print(f"[{ord_list[0].total_weight}", end="")
            for order in ord_list[1:]:
                print(f"<-{order.total_weight}", end="")
    
            print("]", end="\n")
        else:
            print("[*empty*]")
