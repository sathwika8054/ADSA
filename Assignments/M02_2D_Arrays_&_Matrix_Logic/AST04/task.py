def diagonalSort(mat):
    m = len(mat)
    n = len(mat[0])

    # Start from every column of first row
    for col in range(n):
        values = []
        i = 0
        j = col

        # Collect diagonal elements
        while i < m and j < n:
            values.append(mat[i][j])
            i += 1
            j += 1

        # Sort
        values.sort()

        # Put sorted values back
        i = 0
        j = col
        k = 0

        while i < m and j < n:
            mat[i][j] = values[k]
            i += 1
            j += 1
            k += 1

    # Start from every row of first column
    for row in range(1, m):
        values = []
        i = row
        j = 0

        # Collect diagonal elements
        while i < m and j < n:
            values.append(mat[i][j])
            i += 1
            j += 1

        # Sort
        values.sort()

        # Put sorted values back
        i = row
        j = 0
        k = 0

        while i < m and j < n:
            mat[i][j] = values[k]
            i += 1
            j += 1
            k += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())

    mat = []
    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))