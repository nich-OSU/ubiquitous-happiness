import unittest

from linked_lists.lists.nodes import Node, LinkedList
from linked_lists.remove_dupes.main import remove_dupes
from linked_lists.return_kth_to_last.main import return_kth_to_end
from linked_lists.delete_middle_node.main import delete_middle_node
from linked_lists.partition.main import partition
from linked_lists.sum_lists.main import sum_lists_rev, sum_lists_fwd

class CrackingTests_linked_lists(unittest.TestCase):

    def test_2_1(self):
        test_list = LinkedList()
        test_list.appendToStart('a')
        test_list.appendToTail('b')
        test_list.appendToTail('a')
        test_list.appendToTail('b')
        test_list.appendToTail('b')

        expected_list = LinkedList()
        expected_list.appendToStart('a')
        expected_list.appendToTail('b')
        remove_dupes(test_list)

        current_test_node = test_list.head
        current_expected_node = expected_list.head
        while current_test_node is not None and current_expected_node is not None:
            ctn_data = current_test_node.data
            cen_data = current_expected_node.data
            # print(ctn_data, cen_data)
            self.assertEqual(ctn_data, cen_data, f"test: {ctn_data} does not equal expected: {cen_data}")
            current_test_node = current_test_node.next
            current_expected_node = current_expected_node.next

    def test_2_2(self):
        test_list = LinkedList()
        test_list.appendToStart('a')
        test_list.appendToTail('b')
        test_list.appendToTail('c')
        test_list.appendToTail('d')
        test_list.appendToTail('e')

        expected_list = {'1':'e', '2':'d', '3':'c', '4':'b', '5':'a'}
        for i in range(1, 6):
            actual = return_kth_to_end(test_list, i)
            expected = expected_list[str(i)]
            self.assertEqual(actual, expected, f"k:{i} and expected: {expected}")

    def test_2_3(self):
        test_list = LinkedList()
        test_list.appendToStart('a')
        ll_node_b = Node('b')
        test_list.head.next = ll_node_b
        # test_list.appendToTail('b')
        test_list.appendToTail('c')
        test_list.appendToTail('d')
        test_list.appendToTail('e')

        expected_linked_list = LinkedList()
        expected_linked_list.appendToStart('a')
        expected_linked_list.appendToTail('c')
        expected_linked_list.appendToTail('d')
        expected_linked_list.appendToTail('e')

        # ll_node_b = Node('b')
        actual = delete_middle_node(ll_node_b)

        current_test_node = test_list.head
        current_expected_node = expected_linked_list.head
        while current_test_node is not None and current_expected_node is not None:
            ctn_data = current_test_node.data
            cen_data = current_expected_node.data
            # print(ctn_data, cen_data)
            self.assertEqual(ctn_data, cen_data, f"test: {ctn_data} does not equal expected: {cen_data}")
            current_test_node = current_test_node.next
            current_expected_node = current_expected_node.next

    def test_2_4(self):
        pivot = 4
        test_list = LinkedList()
        test_list.appendToStart(1)
        test_list.appendToTail(4)
        test_list.appendToTail(5)
        test_list.appendToTail(6)
        test_list.appendToTail(2)
        test_list.appendToTail(7)
        test_list.appendToTail(3)
        # verify list added
        # test_list.print_linked_list()

        partition(test_list, pivot)
        # test_list.print_linked_list()

        expected_list = [1, 2, 3, 4, 5, 6, 7]
        i = 0
        c_a_n = test_list.head
        while c_a_n is not None:
            # print(c_a_n.data)
            self.assertEqual(c_a_n.data, expected_list[i], f"{i} partition list does not match indexed expected list" )
            c_a_n = c_a_n.next
            i = i + 1

    def test_2_5(self):
        test_list_l1 = LinkedList()
        test_list_l1.appendToTail(7)
        test_list_l1.appendToTail(1)
        test_list_l1.appendToTail(6)
        # test_list_l1.print_linked_list() # REV:7 - 1 - 6 = 617 |\/| FWD: 7 - 1 - 6 = 716

        test_list_l2 = LinkedList()
        test_list_l2.appendToTail(5)
        test_list_l2.appendToTail(9)
        test_list_l2.appendToTail(2)
        test_list_l2.appendToTail(1)
        # test_list_l2.print_linked_list() # REV:5 - 9 - 2 - 1 = 1295 |\/| FWD: 5 - 9 - 2 - 1 = 5921

        actual_summed_listREV = sum_lists_rev(test_list_l1, test_list_l2)   # 617 + 1295 = 1912
        # actual_summed_listREV.print_linked_list()

        actual_summed_listFWD = sum_lists_fwd(test_list_l1, test_list_l2)   # 716 + 5921 = 6637

        expected_summed_l1 = LinkedList()
        expected_summed_l1.appendToTail(2)
        expected_summed_l1.appendToTail(1)
        expected_summed_l1.appendToTail(9)
        expected_summed_l1.appendToTail(1)  # 2 -> 1 -> 9 -> 1

        expected_summed_l2 = LinkedList()
        expected_summed_l2.appendToTail(6)
        expected_summed_l2.appendToTail(6)
        expected_summed_l2.appendToTail(3)
        expected_summed_l2.appendToTail(7)  # 6 -> 6 -> 3 -> 7

        # print("actual resulting summed list in REVERSE")
        # actual_summed_listREV.print_linked_list()
        # print("expected resulting list in REVERSE")
        # expected_summed_l1.print_linked_list()
        cur_anREV = actual_summed_listREV.head
        cur_enREV = expected_summed_l1.head
        node = 1
        while cur_anREV is not None:
            # print(node, cur_anREV.data, cur_enREV.data)
            self.assertEqual(cur_anREV.data, cur_enREV.data, f"Reverse, actual_node:{cur_anREV.data} not equal to exp_node: {cur_enREV.data}")
            cur_anREV = cur_anREV.next
            cur_enREV = cur_enREV.next
            node += 1

        # print("actual_summed_listFWD:")
        # actual_summed_listFWD.print_linked_list()
        # print("expected resulting list in FWD")
        # expected_summed_l2.print_linked_list()

        cur_anFWD = actual_summed_listFWD.head
        cur_enFWD = expected_summed_l2.head
        node = 1
        while cur_anFWD is not None:
            # print(node, cur_anFWD.data, cur_enFWD.data)
            self.assertEqual(cur_anFWD.data, cur_enFWD.data, f"Forward, actual_node:{cur_anFWD.data} not equal to exp_node:{cur_enFWD.data}")
            cur_anFWD = cur_anFWD.next
            cur_enFWD = cur_enFWD.next
            node += 1



if __name__ == '__main__':
    unittest.main()
