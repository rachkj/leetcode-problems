class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Subtree:
    def subtree(self, root:TreeNode, subroot:TreeNode)->bool:
        if not root:
            return False
        if not subroot:
            return True
        if self.isSame(root,subroot):
            return True
        return self.subtree(root.left,subroot) or self.subtree(root.right,subroot)
    
    def isSame(self,s,t):
        if not s and not t:
            return True
        if s and t:
            return s.val==t.val and self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
        
n1=TreeNode(3)
n2=TreeNode(4)
n3=TreeNode(5)
n4=TreeNode(1)
n5=TreeNode(2)

n6=TreeNode(4)
n7=TreeNode(1)
n8=TreeNode(7)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5

n6.left=n7
n6.right=n8

test=Subtree()
print(test.subtree(n1,n6))