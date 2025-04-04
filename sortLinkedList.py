class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class sortLL:
    def sortLL(self, head: ListNode):
        cur=head
        res=[]
        while cur:
            res.append(cur.val)
            cur=cur.next
        res.sort()
        new_head=ListNode(0)
        cur=new_head
        for n in res:
            cur.next=ListNode(n)
            cur=cur.next
        return new_head
    
n1=ListNode(4)
n2=ListNode(2)
n3=ListNode(1)
n4=ListNode(3)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=None

sortLL=sortLL()
sortedHead=sortLL.sortLL(n1)

cur=sortedHead
while cur:
    print(cur.val)
    cur=cur.next