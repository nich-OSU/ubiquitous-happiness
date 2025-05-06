# There are three types of edits that can be performed on strings:
# 1. Insert a character
# 2. Remove a character
# 3. Replace a character
# Write a function that is given two strings to check if they are one or zero edits away.

def insert_test(s1: str, s2: str) -> bool:
    """
    Function to iterate through s1 to see if it is one char away from s2
    Return True if s1 is one char different than s2.
    """
    # positions in the words and
    index1 = 0
    index2 = 0
    # error tracker
    off_by = 0

    while index1 < len(s1) and index2 < len(s2):
        # test for characters the same
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            # keep one index constant and move the other
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def replace_test(s1: str, s2: str) -> bool:
    """
    function to test matching lengths
    returns True if only one char is unmatched
        else returns False if more than one is unmatched
    """
    # reference boolean
    found_difference = False
    # iterate through chars
    for i in range(len(s1)):
        # compare chars
        if s1[i] != s2[i]:

            # check if difference found yet?
            if found_difference:
                return False

            # make reference True
            found_difference = True

    return True

def one_away(s1: str, s2: str) -> bool:
    """
    Function will use helper functions to determine whether input strings are one edit away
    From each other.
    Return True if they are one edit away or false if more than one.
    """
    # check length difference is one or zero
    l1 = len(s1)
    l2 = len(s2)
    if abs(l1 - l2) > 1:
        return False
    # prepare strings for helper functions, find which is longer.
    longer = s1
    shorter = s2
    # if different:
    if l2 > l1:
        longer = s2
        shorter = s1

    # if they are the same length, we will check replacement viability
    if l1 == l2:
        return replace_test(s1, s2)

    # otherwise, check for insertion
    else:
        return insert_test(shorter, longer)

if __name__ == '__main__':
    test_cases = [("pale", "ple"), ("pales", "pale"), ("pale", "bake"), ("valley", "bake")]
    expected_results = [True, True, False, False]
    for index, case in enumerate(test_cases):
        print(index, ":", one_away(case[0], case[1]), expected_results[index])