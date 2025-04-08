
from typing import List
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class MinimumAbsDiff:
    def minAbsDiff(self, root:TreeNode)->TreeNode:
        minDiff=10**20
        sortedRes=sorted(self.inorder(root))
        for i in range(1,len(sortedRes)):
            curDiff=sortedRes[i]-sortedRes[i-1]
            minDiff=min(minDiff,curDiff)
        return minDiff
    
    def inorder(self,root:TreeNode)->List[int]:
        res=[]
        if not root:
            return []
        res+=self.inorder(root.left)
        res.append(root.val)
        res+=self.inorder(root.right)
        return res
    
n1=TreeNode(4)
n2=TreeNode(2)
n3=TreeNode(6)
n4=TreeNode(1)
n5=TreeNode(3)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5

test=MinimumAbsDiff()
print(test.minAbsDiff(n1))