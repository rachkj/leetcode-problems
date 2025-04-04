class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class ValidateBST:
    def validateBST(self, root: TreeNode)->bool:
        def isBST(root,min,max):
            if root is None:
                return True
            if root.val<=min or root.val>=max:
                return False
            return isBST(root.left,min,root.val) and isBST(root.right,root.val, max)
        return isBST(root, float('-inf'), float('inf'))
    
n1=TreeNode(4)
n2=TreeNode(1)
n3=TreeNode(3)

n1.left=n2
n1.right=n3
test=ValidateBST()
print(test.validateBST(n1))