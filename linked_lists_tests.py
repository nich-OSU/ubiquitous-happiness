import unittest

from linked_lists.lists.nodes import Node, LinkedList
from linked_lists.remove_dupes.main import remove_dupes
from linked_lists.return_kth_to_last.main import return_kth_to_end
from linked_lists.delete_middle_node.main import delete_middle_node
from linked_lists.partition.main import partition

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

if __name__ == '__main__':
    unittest.main()
