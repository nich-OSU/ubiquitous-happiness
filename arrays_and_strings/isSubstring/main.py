# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
# one call to isSubstring.

def isSubstring(s1: str, s2: str) -> bool:
    """
    Function to determine if s2 is a rotation of s1.
    Return True or False
    """
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2

if __name__ == "__main__":
    cases =  [
        ("waterbottle", "erbottlewat"),
        ("racecar", "acecarr")
    ]
    for case in cases:
        print(isSubstring(case[0], case[1]))

"""
HINTS:
# 34. If a string is a rotation of another, then its a rotation at a particular point.
The example: cuts waterbottle at 3 and appends the left side to the end of the right.
# 88. Asking if there is a way of splitting the first string into two parts. x and y such that,
the first string xy and the second string is yx.
# 104. Think about the other hints, then think about what happens when you concatenate yx to itself.
"""