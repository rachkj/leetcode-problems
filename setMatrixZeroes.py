from typing import List
class SetMatrixZero:
    def setZeroes(self,matrix:List[List[int]])->List[List[int]]:
        rL=len(matrix)
        cL=len(matrix[0])
        row,col=[1]*rL,[1]*cL
        for i in range(rL):
            for j in range(cL):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0

        for i in range(rL):
            if row[i]==0:
                matrix[i]=[0]*cL

        for j in range(cL):
            if col[j]==0:
                for i in range(rL):
                    matrix[i][j]=0
        return matrix

        

test=SetMatrixZero()
print(test.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(test.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


        

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]