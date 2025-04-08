class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
class KSmallestEle:
    def kSmallestEle(self,root:TreeNode, k:int):
        res=self.inorder(root)
        res.sort()
        return res[k-1]

    def inorder(self,root:TreeNode):
        if not root:
            return []
        res=[]
        res+=self.inorder(root.left)
        res.append(root.val)
        res+=self.inorder(root.right)
        return res
    
n1=TreeNode(3)
n2=TreeNode(1)
n3=TreeNode(4)
n4=TreeNode(2)

n1.left=n2
n1.right=n3
n2.right=n4

test=KSmallestEle()
print(test.kSmallestEle(n1,2))
