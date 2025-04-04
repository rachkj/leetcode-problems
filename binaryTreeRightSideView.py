from collections import deque
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class BTRightSideView:
    def rightsideview(self,root:TreeNode)->List[int]:
        q=deque()
        q.append(root)
        res=[]
        while q:
            lev=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    lev.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lev:
                res.append(lev[-1])
        return res
    
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n1.left=n2
n1.right=n3
n3.right=n4
n2.right=n5

test=BTRightSideView()
print(test.rightsideview(n1))