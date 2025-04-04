class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class MaxDepth:
    def maxDepth(self,root:TreeNode)->int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(2)
n6=TreeNode(4)
n7=TreeNode(7)

n1.left=n2
n1.right=n5
n2.left=n3
n2.right=n4
n5.left=n6
n5.right=n7

test=MaxDepth()
print(test.maxDepth(n1))
    