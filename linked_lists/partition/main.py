# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# Important: The partition element x can appear anywhere in the right partition.
from linked_lists.lists.nodes import Node, LinkedList

def partition(l_list, pivot):
    tail = l_list.head
    count = 1
    while tail.next is not None:
        tail = tail.next
        count = count + 1

    # now tail is pointing at the last node and tail.next is None
    previous = None
    current = l_list.head
    while count > 0:

        if current.data < pivot:
            previous = current
            current = current.next

            count = count - 1

        # current.data >= pivot then move the node to the end
        else:

            # put current at the tail and point tail to current
            tail.next = current
            tail = tail.next

            if previous is None:
                l_list.head = current.next
                current = l_list.head
            else:
                previous.next = current.next
                current = previous.next
            tail.next = None

            count = count - 1


"""
Hints:
3. There are many solutions to this problem, most of which are equally optimal in runtime.
    Some have shorter, cleaner code. Brainstorm different solutions.
24. Consider that the elements dont have to stay in the same relative order. We only need
    to ensure that elements less than the pivot muyst be before elements greatert than the pivot.
"""
