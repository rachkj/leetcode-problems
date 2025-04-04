from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
class BTLevelOrder:
    def levelorder(self, root:TreeNode)->List[List[int]]:
        q=deque()
        res=[]
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
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

test=BTLevelOrder()
print(test.levelorder(n1))