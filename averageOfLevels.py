from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
class AverageOfLevels:
    def levelaverage(self, root:TreeNode)->List[int]:
        q=deque()
        q.append(root)
        res=[]
        while q:
            lev=[]
            for i in range(len(q)):
                n=q.popleft()
                if n:
                    lev.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if lev:
                res.append(sum(lev)/len(lev))
        return res

n1=TreeNode(3)
n2=TreeNode(9)
n3=TreeNode(20)
n4=TreeNode(15)
n5=TreeNode(7)
n1.left=n2
n1.right=n3
n3.left=n4
n3.right=n5

test=AverageOfLevels()
print(test.levelaverage(n1))