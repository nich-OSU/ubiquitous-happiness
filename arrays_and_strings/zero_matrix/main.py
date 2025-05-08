
# Write an algorithm such that if an M x N matrix has an element in it equal to zero,
# Then the row and column will be zeroed out.

def zero_matrix(matrix: list) -> list:
    """
    Function takes in a matrix of M x N dimension and will determine if an element == 0.
    Returns the matrix with row and column of element all changed to zeroes.
    """
    tracker = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                tracker.append((i, j))
    # print(tracker)
    for point in tracker:
        row, column = point
        # print(row)
        # print(column)
        for i in range(len(matrix[row])):
            matrix[row][i] = 0
        for i in range(len(matrix)):
            matrix[i][column] = 0

    return matrix

if __name__ == "__main__":
    test_cases = [
        [[1, 2, 0],
        [2, 4, 7],
        [3, 6, 8]],
        [[1,1,1],[2,2,2],[3,0,3]],
        [[1,1],[0,0]]
    ]
    expected_results = [
        [[0, 0, 0],
        [2, 4, 0],
        [3, 6, 0]],
        [[1, 0, 1], [2, 0, 2], [0, 0, 0]],
        [[0,0],[0,0]]
    ]

    for case in test_cases:
        print(zero_matrix(case))