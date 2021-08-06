def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # for each order in served orders:
        # if the order is takeout[0] or dinein[0]
        # take out the order[0]

    # return False

    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for orders in served_orders:
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders += 1

        else:
            return False

    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False
    
    return True