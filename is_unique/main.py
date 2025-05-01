# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique_hash(s: str) -> bool:
    """
    function to traverse a string to determine if there are any repeated characters.
    hash map is used
    returns boolean
    """
    h = {}
    for c in s:
        if c in h:
            return False
        else:
            h[c] = 1
    return True

def is_unique_no_hash(s: str) -> bool:
    """
    function to traverse a string to determine if there are any repeated characters.
    no hash map is used
    returns boolean
    """
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            print("i: ", s[i], "j: ", s[j])
            if s[i] == s[j]:
                return False
    return True

if __name__ == "__main__":
    test_cases = ["abc", "aabbcc", "abca"]

    for case in test_cases:
        print("hash: ", is_unique_hash(case))
        print("no_hash: ", is_unique_no_hash(case))