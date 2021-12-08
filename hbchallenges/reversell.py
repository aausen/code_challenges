"""Given linked list head node, return head node of new, reversed linked list.

For example:

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
"""


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """
    # 1->2->3->4->5
    # 5->4->3->2->1
    previous = None
    current = head
    next = head.next

    while current:
        if current.next.next != None:
            current.next = previous
            previous = current
            next = current.next.next
            current = current.next
            
        else:
            current.next = previous
            previous = current
            current = current.next

    return current

# 1 p=none, c=1, next=2
# while:
# 1->None
#p=1, c=2, n=3
# 2 p=1, c=2, n=3
# 2->1
# p=2, c=3, n=5 



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")
