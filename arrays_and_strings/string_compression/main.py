# Implement a method to perform basic string compression using the counts
# of repeated characters. The compressed string will be composed of alpha characters
# and numeric characters. If the compressed string would not become smaller,
# return the original string. Assume the string only has upper and lower case letters.

def string_compression(s: str) -> str:
    """
    Function to take in a string and compress repeated characters into shorter string.
    Return a string compressed.
    """
    count = 1
    char = ""
    result = ""
    for i in range(len(s)):
        # starting char
        if i == 0:
            char = s[i]
            continue
        else:
            if char == s[i]:
                count += 1
            if char != s[i]:
                # update the result
                result += char
                result += str(count)

                # reset the counter and char
                char = s[i]
                count = 1

            # clean up if last time around
            if i + 1 == len(s):
                result += char
                result += str(count)

    # check if the compression improves our string length
    if len(s) > len(result):
        return result
    else:
        return s


if __name__ == '__main__':
    test_cases = ["aabcccccaaa", "abcdee", "aaabbaaac"]
    expected_results = ["a2b1c5a3", "abcdee", "a3b2a3c1"]
    for case in test_cases:
        print(string_compression(case))

"""
HINTS:
92. Do the easy thing first. Compress the string, then compare the lengths.
110. Do not repeatedly concatenate strings together, this is inefficient.
"""