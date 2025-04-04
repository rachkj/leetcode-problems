class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class removeDuplicates:
    def removeDupFromSortedLL(self, head:ListNode):
        s=set()
        prev=ListNode(0)
        prev.next=head
        cur=head
        while cur:
            if cur.val not in s:
                s.add(cur.val)
            else:
                prev.next=cur.next
            prev=cur
            cur=cur.next
        return head
    
n1=ListNode(1)
n2=ListNode(1)
n3=ListNode(2)
n4=ListNode(3)
n5=ListNode(3)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

remDup=removeDuplicates()
newHead=remDup.removeDupFromSortedLL(n1)

while newHead:
    print(newHead.val)
    newHead=newHead.next


        