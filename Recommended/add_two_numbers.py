# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return "Hello"
    

l1 = [2,4,3]
l2 = [5,6,4]

solution = Solution()
print(solution.addTwoNumbers(l1,l2))