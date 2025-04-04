# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy=ListNode()
        cur=dummy
        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        while list1:
            cur.next=list1
            list1=list1.next
            cur=cur.next
        while list2:
            cur.next=list2
            list2=list2.next
            cur=cur.next
        return dummy.next
    
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(4)


n4=ListNode(1)
n5=ListNode(3)
n6=ListNode(4)

n1.next=n2
n2.next=n3
n3.next=None


n4.next=n5
n5.next=n6
n6.next=None


mergeList=Solution()
newHead=mergeList.mergeTwoLists(n1,n4)

while newHead:
    print(newHead.val)
    newHead=newHead.next