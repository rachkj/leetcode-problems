class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class PalindromicLL:
    def palindromicLL(self, head:ListNode)->bool:
        res=[]
        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        return res==res[::-1]
    
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(2)
n4=ListNode(1)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=None

pal=PalindromicLL()
print(pal.palindromicLL(n1))