from typing import List
class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class PreOrderDFS:
    def preOrderDFS(self, root:TreeNode)->List[int]:
        if not root:
            return []
        st=[]
        res=[]
        st.append(root)
        while st:
            node=st.pop()
            if node:
                res.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return res
    
n1=TreeNode(3)
n2=TreeNode(9)
n3=TreeNode(20)
n4=TreeNode(15)
n5=TreeNode(7)
n1.left=n2
n1.right=n3
n3.left=n4
n3.right=n5

test=PreOrderDFS()
print(test.preOrderDFS(n1))

