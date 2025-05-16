# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed.
from linked_lists.lists.nodes import Node, LinkedList

def remove_dupes(ll_node):
    hash_map = {}
    current = ll_node.head
    previous = None
    while current is not None:
        if current.data not in hash_map:
            hash_map[current.data] = 1
            previous = current
        else:
            # remove the duplicate
            previous.next = current.next

        current = current.next

"""
HINTS:
#####
9. Have you tried a hash table? You should be able to do this in a single pass of the linked list.
40. Without extra space, you'll need O(N^2) time.
Try using two pointers, where the second one searches ahead of the first.
"""