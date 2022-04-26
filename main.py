from methods import *
from classes import *

shop_status           = True
processing_queue_len  = 5
initial_pending_queue = []

# main:
clear()

pending, processing, fulfilled = initialize_data_structures(initial_pending_queue)
counter = 1

coffee_kitchen = Kitchen(pending, processing, fulfilled, processing_queue_len)

while shop_status is True:
    print("--------Welcome to Coffee Shop--------\n")
    display_menu(coffee_kitchen)

    choice = input("Do you want to (P)lace new order or (E)xecute old order [P/E]: ").lower()
    print()

    if choice == 'p':
        print_orders(coffee_kitchen)

        item_list = place_order()
    
        coffee_kitchen.add_order(counter, item_list, get_time())
        print("Order Placed!!")
        counter = counter + 1

        print_orders(coffee_kitchen)

    elif choice == 'e':
        print_orders(coffee_kitchen)

        coffee_kitchen.process()

        if coffee_kitchen.processing != []:
            coffee_kitchen.current_order.print_order()
            processing_anim(0.2, coffee_kitchen.current_order.order_num)
        else:
            print("No orders to process!!")

        print_orders(coffee_kitchen)
        input("Press Enter to continue...")

    elif choice == 'q':
        shop_status = False
    
    clear()
