from typing import List
class RotateImage:
    def rotateImage(self, matrix:List[List[int]])->List[List[int]]:
        n=len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

        for i in range(len(matrix)):
            head=0
            tail=len(matrix)-1
            while head<tail:
                temp=matrix[i][head]
                matrix[i][head]=matrix[i][tail]
                matrix[i][tail]=temp
                head+=1
                tail-=1
        return matrix

test=RotateImage()
print(test.rotateImage([[1,2,3],[4,5,6],[7,8,9]]))
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]