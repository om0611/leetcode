'''
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each 
node in the linked list is either 0 or 1. The linked list holds the binary 
representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
'''

# Key Ideas:
# Reverse the linked list so that we can iterate through the number in 
# increasing powers of 2. Initialize the result to be 0 and the current power
# of 2 to be 1. While we don't reach the end of the linked list:
#   - if the current node's value is 1, we add the current power to the result 
#   - multiply the current power by 2
# At the end, we return the result.


# Runtime: O(n) because we are passing through the linked list twice while 
# doing constant work during each iteration. 

# Space: O(1) because we are only storing an integer in memory. 


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Reverse the linked list
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        
        res = 0
        curr_power = 1
        curr = prev
        while curr:
            if curr.val:
                res += curr_power
            curr_power *= 2
            curr = curr.next
        
        return res