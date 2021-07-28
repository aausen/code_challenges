import unittest

def contains_cycle(head):
    # looks through each node in the ll
    # set current node
    current = head
    # keep track of nodes we have seen in set
    seen = set()
    while current:
        # if we see node again, return True
        if current in seen:
            return True
        # if the current node is none, we hit the end so return False
        elif current == None:
            return False
        # else add the current node to our set and keep looping
        else:
            seen.add(current)
            current = head.next

# Tests
class Test(unittest.TestCase):

    class LinkedListNode(object):
        
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def test_linked_list_with_no_cycle(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle(first)
        self.assertTrue(result)


unittest.main(verbosity=2)