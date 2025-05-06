# Given a string, write a function to check if it is a permutation of a palindrome.
# The palindrome is a rearrangement of letters, such that the word or phrase is the same
# backwards as it is forward.
# The palindrome does not need to be just dictionary words and non-letter and casing can be ignored.

def palindrome_permutation(s: str) -> bool:
    """
    Function to examine input string and determine if a permutation is a palindrome.
    Returns True if palindrome can be made, else False.
    """
    memo = {}
    s_arr = [c.lower() for c in list(s) if c.isalpha()]
    for c in s_arr:
        if c in memo:
            memo[c] += 1
        else:
            memo[c] = 1

    # examine the memo all keys should be even with only one allowed as odd.
    odd = 0
    even = 0
    for key in memo:
        if memo[key] % 2 == 0:
            even += 1
        if memo[key] % 2 == 1:
            odd += 1
    if odd > 1:
        return False

    return True

if __name__ == "__main__":
    test_cases = [
        "tactc oa",
        "cacaco",
        "a Toyota",
        "oy ban3ana boy"
    ]

    for case in test_cases:
        print(palindrome_permutation(case))