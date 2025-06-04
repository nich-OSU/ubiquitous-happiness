# Make a function that takes in two linked lists, where each node contains a single digit.
# Do two functions one where the digits are stored in reverse order and one where they are stored in forward order.
from linked_lists.lists.nodes import Node, LinkedList

def sum_lists_rev(ll_1: LinkedList, ll_2: LinkedList) -> LinkedList:
    # set current node to top of each linked list.
    cur_n1, cur_n2 = ll_1.head, ll_2.head
    # build resultant Linked List and carryover variables
    res_ll = LinkedList()
    carryover = 0

    # iterate through each linked list until both are None
    while cur_n1 is not None or cur_n2 is not None:
        # conditional for when linked list is empty
        n1_data = 0 if cur_n1 is None else cur_n1.data
        n2_data = 0 if cur_n2 is None else cur_n2.data

        # calculations:
        sum_of_nodes = carryover + n1_data + n2_data
        node_data = sum_of_nodes % 10
        carryover = sum_of_nodes // 10

        # build the result linked list backwards
        res_ll.appendToTail(node_data)

        # cycle to next node
        cur_n1 = None if (cur_n1 is None or (cur_n1.next is None)) else cur_n1.next
        cur_n2 = None if (cur_n2 is None or(cur_n2.next is None)) else cur_n2.next

    if carryover:
        res_ll.appendToTail(carryover)

    return res_ll

def sum_lists_fwd(ll_1: LinkedList, ll_2: LinkedList) -> LinkedList:
    # set current node to top of each linked list.
    cur_n1, cur_n2 = ll_1.head, ll_2.head
    c1_len, c2_len = 0, 0

    # Finding the length of each linked list:
    while cur_n1 is not None:
        c1_len += 1
        cur_n1 = cur_n1.next
    while cur_n2 is not None:
        c2_len += 1
        cur_n2 = cur_n2.next

    res_ll = LinkedList()

    # reset variables
    cur_n1, cur_n2 = ll_1.head, ll_2.head
    res_cur = res_ll.head
    res_prev_node = None

    while c1_len != c2_len:
        if c1_len > c2_len:
            if res_cur is None:
                res_ll.appendToTail(cur_n1.data)
                # res_ll.print_linked_list()
                res_cur = res_ll.head
            cur_n1 = cur_n1.next
            c1_len -= 1
        if c2_len > c1_len:
            if res_cur is None:
                res_ll.appendToTail(cur_n2.data)
                # res_ll.print_linked_list()
                res_cur = res_ll.head
                # print("1:", res_ll.head.data)
            cur_n2 = cur_n2.next
            c2_len -= 1
        res_prev_node = res_cur

    # print("res_current", res_cur)
    # print("res_prev_node",res_prev_node)

    while c1_len > 0:
        sum_of_nodes = cur_n1.data + cur_n2.data
        tail_node = sum_of_nodes % 10
        prev_carryback = sum_of_nodes // 10
        if res_prev_node is None:
            if prev_carryback > 0:
                res_ll.appendToTail(prev_carryback)
                res_cur = res_ll.head
            res_ll.appendToTail(tail_node)

        else:
            res_prev_node.data = res_prev_node.data + prev_carryback
            res_ll.appendToTail(tail_node)

        # adjust pointer variables
        c1_len -= 1
        c2_len -= 1
        cur_n1 = cur_n1.next
        cur_n2 = cur_n2.next
        res_prev_node = res_cur
        res_cur = res_cur.next

    return res_ll

"""
HINTS:
7. Convert the linked lists to integers, compute the sum, and then convert it back to a new linked list.
30. Try recursion, suppose with two lists: A = 1->5->9 (951) and B = 2->3->6->7 (7632) a function to
operate on the remainder of the lists.
71. Make sure you have considered linked lists that are not of the same length
95. Does you algorithm work on linked lists like 9-7-8 and 6-8-5?
109. For the follow up question: the issue is that when the linked lists arent the same ength, the head of one linked list might represent the 1000s place while the other represents the 10s place.
"""