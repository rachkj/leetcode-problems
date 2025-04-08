from typing import List
class Search2DMatrix:
    def searchMatrix(self, matrix:List[List[int]], target: int)->bool:
        rowL=len(matrix)
        colL=len(matrix[0])
        top,bottom=0,rowL-1
        while top<=bottom:
            row=(top+bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break

        if top>bottom:
            return False

        l,r=0,colL-1
        while l<=r:
            m=(l+r)//2
            if target==matrix[row][m]:
                return True
            elif target<matrix[row][m]:
                r=m-1
            else:
                l=m+1
        return False

test=Search2DMatrix()
print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

        

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
