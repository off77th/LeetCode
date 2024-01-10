# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.val)
    
def printLinkedList(linked_list):
    if linked_list is None:
        print("Empty list")
        return
    current = linked_list
    while current is not None:
        print (current, end= " ")
        current = current.next
    print()


# Previous
#   current = empty = ListNode() 
#   while head:
#         if current.val != head.val:
#             current.next = ListNode(head.val)
#             current = current.next
#         head = head.next
#   return empty.next
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val != current.next.val:
                current = current.next
            else:
                current.next = current.next.next

        return head


l1 = ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(2)

printLinkedList(l1)


solution = Solution()
printLinkedList(solution.deleteDuplicates(l1))