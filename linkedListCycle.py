class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class LinkedListCycle:
    def linkedlistCycle(self, head:ListNode):
        cur=head
        visited=[]
        while cur:
            if cur not in visited:
                visited.append(cur)
                cur=cur.next
            else:
                return True
        return False
    

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2 

llcycle=LinkedListCycle()
print(llcycle.linkedlistCycle(node1)) 