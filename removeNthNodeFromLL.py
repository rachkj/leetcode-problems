class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class RemoveNthNodeFromLL:
    def removeNthNodeFromLL(self,head:ListNode,n:int):
        start=ListNode(0)
        start.next=head
        slow=start
        fast=start
        cur=start.next
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return start.next
    
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
n5=ListNode(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

ll=RemoveNthNodeFromLL()
newHead=ll.removeNthNodeFromLL(n1,2)

cur=newHead
while cur:
    print(cur.val)
    cur=cur.next