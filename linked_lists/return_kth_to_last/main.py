# Create an algorithm to find the kth to lasst element
# of a singly linked list.
from linked_lists.lists.nodes import Node, LinkedList

def return_kth_to_end(linked_list, k) -> str:
    ll_length = linked_list.sizeLinkedList()
    count = ll_length - k
    
    if count < 0 or ll_length == 0:
        return None
    # ll is as big or bigger than k
    current = linked_list.head

    # iterate through list until count is zero
    while count > 0:
        current = current.next
        count = count - 1

    return current.data


"""hints:
# 8. What if you knew the linked list size? What is the difference
between finding the kth to last element and finding the xth element.
# 25. If you don't know the linked list size, can you compute it? How does
this impact the run time?
# 41. Try implementing it recursively. If you could find the K-1 item,
can you find the kth element?
# 67. You might find it useful to return multiple values. Some languages
don't support this, but there are workarounds in essentially any lnaguage.
What are some workarounds?
# 126. Can you do it iteratively? Imagine if you had two pointers pointing to adjacent nodes
and they were moving at the same speed through the linked list.
When one hist the end, where will the other one be?
"""

if __name__ == '__main__':
    pass