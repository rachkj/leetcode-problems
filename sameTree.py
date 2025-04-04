class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
class SameTree:
    def sameTree(self, p: TreeNode, q:TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
    
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)

n1.left=n2
n1.right=n3

n4=TreeNode(1)
n5=TreeNode(2)
n6=TreeNode(4)

n4.left=n5
n4.right=n6

test=SameTree()
print(test.sameTree(n1,n4))
