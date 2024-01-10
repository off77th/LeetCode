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


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        empty = ListNode()
        current = empty

        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else: 
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return empty.next

l1 = ListNode(-9)
l1.next=ListNode(3)

l2 = ListNode(5)
l2.next=ListNode(7)

printLinkedList(l1)
printLinkedList(l2)


solution = Solution()
printLinkedList(solution.mergeTwoLists(l1,l2))