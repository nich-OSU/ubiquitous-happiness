import unittest

from linked_lists.lists.nodes import Node, LinkedList
from linked_lists.remove_dupes.main import remove_dupes
from linked_lists.return_kth_to_last.main import return_kth_to_end

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


if __name__ == '__main__':
    unittest.main()