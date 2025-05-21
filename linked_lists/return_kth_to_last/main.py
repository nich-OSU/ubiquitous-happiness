# Create an algorithm to find the kth to last element
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
    I implemented with this hint in mind. Count will count up to the difference in length and k.
    Also implemented a length of linked_list function.
    O(n+n-k) -> O(2n-k) => O(n)
# 25. If you don't know the linked list size, can you compute it? How does
this impact the run time?
    Without knowing the length, I would iterate once through the list.
    It is possible to iterate once through and put the items into a hash map, to then call on the length-kth item in the hash.
# 41. Try implementing it recursively. If you could find the K-1 item,
can you find the kth element?

# 67. You might find it useful to return multiple values. Some languages
don't support this, but there are workarounds in essentially any lnaguage.
What are some workarounds?
# 126. Can you do it iteratively? Imagine if you had two pointers pointing to adjacent nodes
and they were moving at the same speed through the linked list.
When one hist the end, where will the other one be?
    I liked this. Iterate one pointer k items into the list. Then make second pointer at front
    of the list and iterate both one at a time until the first pointer is at the end, then the second one
    is k items back.
"""

if __name__ == '__main__':
    pass