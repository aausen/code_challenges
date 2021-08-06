import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # for each order in served orders:
        # if the order is takeout[0] or dinein[0]
        # take out the order[0]

    # return False

    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        else:
            return False

    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False
    
    return True

# Tests
class Test(unittest.TestCase):

    def test_both_registers_have_same_num_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [1, 2, 3], [1, 2, 3])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 2], [3, 4, 5, 6], [1, 2, 4, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 3], [2, 5, 6], [1, 2, 3, 4, 5, 6])
        self.assertFalse(result)

    def test_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6, 7], [1, 2, 4, 5, 6, 7])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([45, 3, 5], [2, 65, 34, 55], [45, 3, 65, 5, 34, 55])
        self.assertFalse(result)

    def test_orders_are_not_sequential(self):
        result = is_first_come_first_served([77, 3, 22, 5], [1, 55, 33, 2], [77, 1, 3, 22, 55, 5, 33, 2])
        self.assertTrue(result)

unittest.main(verbosity=2)