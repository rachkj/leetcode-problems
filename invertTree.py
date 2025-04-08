from collections import deque
class TreeNode:
    def __init__(self, val=0,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class InvertTree:
    def invertTree(self,root:TreeNode)->TreeNode:
        if not root:
            return None
        
        temp=root.left
        root.left=root.right
        root.right=temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
def BST(root:TreeNode):
    if not root:
        return None
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
    print(res)
        
    
n1=TreeNode(4)
n2=TreeNode(2)
n3=TreeNode(7)
n4=TreeNode(1)
n5=TreeNode(3)
n6=TreeNode(6)
n7=TreeNode(9)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

test=InvertTree()
new_root=test.invertTree(n1)
BST(new_root)
    


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]