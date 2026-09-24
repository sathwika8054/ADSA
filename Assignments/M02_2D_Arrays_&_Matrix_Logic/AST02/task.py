from typing import List

def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    zero_rows = set()
    zero_cols = set()

    # Find rows and columns containing 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set corresponding rows and columns to 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix


if __name__ == '__main__':
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        row = list(map(int, line.split()))
        matrix.append(row)

    print(setZeroes(matrix))
