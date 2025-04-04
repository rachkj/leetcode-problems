class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class SymmericTree:
    def symmetricTree(self, root:TreeNode)->bool:
        def isMirror(self,n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val==n2.val and isMirror(self,n1.left, n2.right) and isMirror(self,n1.right, n2.left)
        return isMirror(self,root.right,root.left)



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

test=SymmericTree()
print(test.symmetricTree(n1))