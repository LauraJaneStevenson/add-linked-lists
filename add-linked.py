class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # get sum of two numbers 
    new_num = int(l1.as_rev_string()) + int(l2.as_rev_string())

    # create list where we will store Nodes
    temp_lst = []

    # create nodes out of reversed new_num
    i = len(str(new_num)) - 1
    
    while i >= 0:
 
        temp_lst.append(Node(int(str(new_num)[i])))

        i -= 1


    # link nodes together
    for i in range(len(temp_lst)):

        # conditional so we won't go out of range
        if i != len(temp_lst) - 1:

            temp_lst[i].next = temp_lst[i+1]

    # return head node
    return temp_lst[0]


l1 = Node(3, Node(2, Node(1)))
l2 = Node(6, Node(5, Node(4)))









