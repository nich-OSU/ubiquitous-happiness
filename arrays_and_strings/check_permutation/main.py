#  Given two strings, write a method to decide if one is a permutation of the other.
def check_permutation(s1: str, s2: str) -> bool:
    """
    function checks whether s1 is a permutation of s2
    returns true if s1 has same length and same frequency of characters as s2
    else returns false
    """
    h = {}
    # length test
    if len(s1) != len(s2):
        return False
    # frequency test
    # populate character count in hash map for first string
    for c in s1:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1

    # validate second string with hash map and process character counts
    for c in s2:
        if c in h:
            h[c] -= 1
        # if a character is in s2 but not s1, return false
        else:
            return False

    # check counts of characters in hash map after processing
    for key in h:
        if h[key] != 0:
            return False

    # counts match up then permutation is true
    return True

def check_permutation_sorted(s1: str, s2: str) -> bool:
    """
    function will take two strings and sort the characters,
    returns true for s1 permutation of s2
    else false
    """
    if len(s1) != len(s2):
        return False

    # Sort
    s1_sorted = sorted(list(s1))
    s2_sorted = sorted(list(s2))
    for i in range(len(s1)):
        if s1_sorted[i] != s2_sorted[i]:
            return False
    return True

if __name__ == "__main__":
    test_cases = [
        ("abcdddd","aaaabcd"),
        ("rats", "star"),
        ("aabbcdd","abcdabd"),
        ("1234567890","0004567890")
        ]
    for case in test_cases:
        print("unsorted: ", check_permutation(case[0], case[1]))
        print("sorted: ",check_permutation_sorted(case[0], case[1]))

#########
# Hints:
#########
# 1. Describe what it means for two strings to be permutations of each other.
    # Look at that definition you provided.
    # Can you check the strings against that definition?
        # permutation is that the same characters are in both with the same frequency
# 84. There is one solution that is O(N log N) time.
    # Another solution uses some space but is O(N) time.
# 122. Could a hash table be useful?
# 131. Two strings that are permutations should have the same characters but in different
    # orders. Can you make the orders the same?