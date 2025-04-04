from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None)->List[int]:
        self.val=val
        self.left=left
        self.right=right
class Inorder:
    def inorder(self, root):
        res=[]
        if not root:
            return res
        res+=self.inorder(root.left)
        res.append(root.val)
        res+=self.inorder(root.right)
        return res
n1=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n1.right=n2
n2.left=n3
test=Inorder()
print(test.inorder(n1))

