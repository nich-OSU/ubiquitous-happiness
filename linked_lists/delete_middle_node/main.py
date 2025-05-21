# Implement an algorithm to delete a node in the middle of a singly linked list
# given only access to that node.
from linked_lists.lists.nodes import Node, LinkedList

def delete_middle_node(ll_node):
    if (ll_node.data is None) or (ll_node.next is None):
        return False

    next = ll_node.next
    ll_node.data = next.data
    ll_node.next = next.next
    return True


"""
Hints:
72. Picture the list 1 -> 5 -> 9 -> 12. Removing 9 would make it look like
    1->5->12.
    You only have access to the 9 node. Can you make it look like the correct answer?
"""

if __name__ == '__main__':
    pass