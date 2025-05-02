# Write a method to replace all spaces in a string with '%20'.
# Assume that the string has sufficient space at the end to hold the additional characters
# and that you are given the True length of the string.
# Example: "Mr John Smith    ", 13  = "Mr%20John%20Smith"

def urlify(s1: str, len1: int) -> str:
    """
    Function will take a string and a true length of the string from start to last char.
    returns a string with spaces removed.
    """
    result = ""
    for i in range(len1):
        if s1[i] == " ":
            result = result + "%20"
        else:
            result += s1[i]
    s1 = result
    return s1

if __name__ == "__main__":
    test_cases = [("abc", 3), ("ab c", 4), ("ab c   ", 4), ("Mr John Smith", 13)]
    for case in test_cases:
        print(urlify(case[0], case[1]))

########
# Hints
########
# 53. It's often easiest to modify strings by going from
#   the end of the string to the beginning
# 118. You might find you need to know the number of spaces. Can you just count them?