from typing import List
from collections import deque
class NumberOfIslands:
    def numOfIslands(self, grid:List[List[int]])->int:
        visited=set()
        islands=0
        rows=len(grid)
        cols=len(grid[0])
        if not grid:
            return 0
        
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r,c=q.popleft()
                dir=[[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in dir:
                    if r+dr in range(rows) and c+dc in range(cols) and (r+dr, c+dc) not in visited and grid[r+dr][c+dc]=='1':
                        visited.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    islands+=1
        return islands
    

test=NumberOfIslands()
print(test.numOfIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

        
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1