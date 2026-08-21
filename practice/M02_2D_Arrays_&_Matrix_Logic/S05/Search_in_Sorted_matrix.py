#74 Traditional the drawback was space complexity 
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        a=[]
        for row in matrix:
            a+=row
        left =0
        right = len(a)-1
        while left<=right:
            mid=(left+right)//2
            if a[mid]==target:
                return True
            elif a[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))

#optimal solution 
def searchMatrixs(matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while left <=right:
            mid=(left+right)//2
            row,col=mid//n,mid%n
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                right=mid-1
            else:
                left=mid+1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrixs(matrix,target))


#240
def SearchMatrix(matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        r,c=0,n-1
        while r<m and c>=0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c-=1 
            else:
                r+=1 
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(SearchMatrix(matrix,target))