import unittest

from arrays_and_strings.is_unique.main import is_unique_hash, is_unique_no_hash
from arrays_and_strings.check_permutation.main import check_permutation, check_permutation_sorted
from arrays_and_strings.urlify.main import urlify
from arrays_and_strings.palindrome_permutation.main import palindrome_permutation
from arrays_and_strings.one_away.main import one_away, replace_test, insert_test
from arrays_and_strings.string_compression.main import string_compression
from arrays_and_strings.rotate_matrix.main import rotate_matrix

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

    def test_1_2(self):
        cases = [
            ("abcdddd","aaaabcd"),
            ("rats", "star"),
            ("aabbcdd","abcdabd"),
            ("1234567890","0004567890")
            ]
        expected_results = [False, True, True, False]
        for index, case in enumerate(cases):
            actual = check_permutation(case[0], case[1])
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"{case}-> a:{actual} does not equal e:{expected}")
            actual = check_permutation_sorted(case[0], case[1])
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"(SORTED){case}-> a:{actual} does not equal e:{expected}")

    def test_1_3(self):
        cases = [
            ("abc", 3),
            ("ab c", 4),
            ("ab c   ", 4),
            ("Mr John Smith", 13)
            ]
        expected_results = [
                "abc",
                'ab%20c',
                'ab%20c',
                "Mr%20John%20Smith"
            ]
        for index, case in enumerate(cases):
            actual = urlify(case[0], case[1])
            expected =  expected_results[index]
            self.assertEqual(actual, expected, f"{case}, a:{actual} does not equal e:{expected}")

    def test_1_4(self):
        cases = [
            "Tact Coa",
            'carr ece',
            'yoda toy'
            ]
        expected_results = [
            True,
            True,
            False
            ]
        for index, case in enumerate(cases):
            actual = palindrome_permutation(case)
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"{case}: a: {actual}, e: {expected}")

    def test_1_5(self):
        cases = [
            ("pale", "ple"),
            ("pales", "pale"),
            ("pale", "bale"),
            ("pale", "bake")
        ]
        expected_results = [True, True, True, False]
        for index, case in enumerate(cases):
            actual = one_away(case[0], case[1])
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"{case}, a: {actual}, e: {expected}")

    def test_1_6(self):
        cases = ["aabcccccaaa", "abcdee", "aaabbaaac"]
        expected_results = ["a2b1c5a3", "abcdee", "a3b2a3c1"]
        for index, case in enumerate(cases):
            actual = string_compression(case)
            expected = expected_results[index]
            self.assertEqual(actual, expected, f"{case}, a:{actual}, e:{expected}")

    def test_1_7(self):
        cases = [
            [[1, 2],
            [3, 4]],
            [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]],
            [],
            [[1, 2, 3], [3]],
            [["a", "b", "c"],
            ["d", "e", "f"],
            ['g', 'h', 'i']]
            ]
        expected_results = [
            [[3, 1],
            [4, 2]],
            [[6, 3, 0],
            [7, 4, 1],
            [8, 5, 2]],
            False,
            False,
            [["g", "d", "a"],
            ["h", "e", "b"],
            ['i', 'f', 'c']]
            ]
        for index, case in enumerate(cases):
            actual = rotate_matrix(case)
            expected = expected_results[index]
            if not expected:
                self.assertFalse(actual, f"{index} test failed -> e:{expected} and actual: {actual}")
            else:
                for i, row in enumerate(actual):
                    for j, column in enumerate(row):
                        self.assertEqual(column, expected[i][j], f"column in row of actual = {actual[i][j]} not expected: {expected[i][j]}")



if __name__ == '__main__':
    unittest.main()