class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class SearchInBST:
    def searchInBST(self,root:TreeNode,val:int)->TreeNode:
        if not root:
            return None
        
        if root.val==val:
            return root
        if val<root.val:
            return self.searchInBST(root.left,val)
        else:
            return self.searchInBST(root.right,val)
        
n1=TreeNode(4)
n2=TreeNode(2)
n3=TreeNode(7)
n4=TreeNode(1)
n5=TreeNode(3)


n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5

test=SearchInBST()
newRoot=test.searchInBST(n1,2)



        