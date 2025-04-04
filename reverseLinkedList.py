class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class ReverseLinkedList:
    def reverseLinkedList(self, head: ListNode):
        prev=None
        cur=head
        while cur:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        return prev

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)
n5=ListNode(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None

reverseLL=ReverseLinkedList()
reversedHead=reverseLL.reverseLinkedList(n1)

cur=reversedHead
while cur:
    print(cur.val)
    cur=cur.next



# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]