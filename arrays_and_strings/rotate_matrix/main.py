# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer,
# write a method to rotate the image by 90 degrees.

def rotate_matrix(matrix: list) -> list:
    """
    Function that will rotate the n x n matrix by 90 degres
    Return a matrix
    """
    l = len(matrix)
    if l == 0 or l != len(matrix[0]):
        return False

    new_matrix = [[None for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            new_matrix[j][l - 1 - i] = matrix[i][j]

    return new_matrix


if __name__ == '__main__':
    test_cases = [
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

    for index, case in enumerate(test_cases):
        print(rotate_matrix(case), expected_results[index])