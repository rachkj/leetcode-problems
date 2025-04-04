class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class RemoveNode:
    def removeNode(self,head:ListNode, val: int)->ListNode:
        cur=head
        prev=ListNode(0)
        prev.next=cur
        while cur:
            if cur.val==val:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next  
        return head
    

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(6)
n4=ListNode(3)
n5=ListNode(4)
n6=ListNode(5)
n7=ListNode(6)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7

newL=RemoveNode()
newH=newL.removeNode(n1,6)
while newH:
    print(newH.val)
    newH=newH.next
