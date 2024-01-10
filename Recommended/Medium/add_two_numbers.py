# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.val)
                   

class LinkedList:
    def __init__(self, list=None) -> None:
        self.head = ListNode(list[0])
        current = self.head
        for value in list[1:]:
            current.next = ListNode(value)
            current = current.next
    
    def print(self):
        if not self.head:
            print("List is empty")
            return
        current=self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


# l1 = LinkedList([5,6,4])
# l1.print()
# l2 = LinkedList([2,4,3])

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        current = temp
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summ = x + y + carry

            carry = summ // 10
            value = summ % 10
            current.next = ListNode(value)
            current=current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)

        return temp.next
    
    def printList(self, linked_list):
        if linked_list is None:
            print("Empty list")
            return
        current = linked_list
        while current is not None:
            print (current, end= " ")
            current = current.next
        print()
        

l1 = ListNode(5)
l1.next=ListNode(6)
l1.next.next=ListNode(4)

l2 = ListNode(2)
l2.next=ListNode(4)
l2.next.next=ListNode(3)


solution = Solution()
solution.printList(l1)
solution.printList(l2)
print(solution.addTwoNumbers(l1,l2))
