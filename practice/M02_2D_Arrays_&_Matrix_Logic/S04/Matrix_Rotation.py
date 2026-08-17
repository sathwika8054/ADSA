#48
def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
            i.reverse()
        return matrix
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))

#1886
def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for _ in range(4):
            if mat==target:
                return True
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in mat:
                i.reverse()
        return False
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(findRotation(mat,target))