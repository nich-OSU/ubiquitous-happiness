import unittest

from is_unique.main import is_unique_hash, is_unique_no_hash
from check_permutation.main import check_permutation, check_permutation_sorted
from urlify.main import urlify

class CrackingTests(unittest.TestCase):

    def test_1_1_hash(self):
        cases = ["abc", "aabbcc", "abca", "abcdprstp"]
        expected_results = [True, False, False, False]
        for index, case in enumerate(cases):
            actual = is_unique_hash(case)
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"i:{case}, a:{actual} does not equal e:{expected}")

    def test_1_1_no_hash(self):
        cases = ["abc", "aabbcc", "abca", "abcdprstp"]
        expected_results = [True, False, False, False]
        for index, case in enumerate(cases):
            actual = is_unique_hash(case)
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"i:{case}, a:{actual} does not equal e:{expected}")

if __name__ == '__main__':
    unittest.main()