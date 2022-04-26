from methods import *
from classes import *
import random

shop_status           = True
processing_queue_len  = 5
initial_pending_queue = []

# main:
clear()

pending, processing, fulfilled = initialize_data_structures(initial_pending_queue)
#counter = 11

coffee_kitchen = Kitchen(pending, processing, fulfilled, processing_queue_len)

def stress_test(lenrange, srange, erange):
    n = random.randint(2, lenrange)
    a = [random.randint(srange, erange) for x in range(0, n)]

    return a

samples  = 20
lenrange = 6
srange   = 1
erange   = 12

cnt = 1
while cnt<=samples:
    order = stress_test(lenrange, srange, erange)
    coffee_kitchen.add_order(cnt, order, get_time())
    cnt = cnt + 1

initial_sequence = list(coffee_kitchen.pending.queue)

print("--------Welcome to Coffee Shop--------\n")
display_menu(coffee_kitchen)

while shop_status is True:
    print_orders(coffee_kitchen)

    coffee_kitchen.process()

    if coffee_kitchen.processing != []:
        coffee_kitchen.current_order.print_order()
        processing_anim(0.01, coffee_kitchen.current_order.order_num)
    else:
        print("No orders to process!!")
        print_orders(coffee_kitchen)
        break

# report:

print("Report:")
print("------------------------------------------------------------------------------------------------------------------------")
print()
print_ord_wgt("Sequence in which orders were received   : ", initial_sequence                    , type="ord")
print("\n")
print_ord_wgt("Sequence in which orders were fulfilled  : ", list(coffee_kitchen.fulfilled.queue), type="ord")
print()
print("------------------------------------------------------------------------------------------------------------------------")
#print()
#print_ord_wgt("Sequence in which weights were received  : ", initial_sequence                    , type="wgt")
#print("\n")
#print_ord_wgt("Sequence in which weights were fulfilled : ", list(coffee_kitchen.fulfilled.queue), type="wgt")
