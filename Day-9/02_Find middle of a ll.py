# Find Middle of a linkedlist

# Approach-1:
# We can count total no. of nodes in ll 
# coz we need to return 2nd mid so mid = n//2+1
# again traverse and reach at mid node and return


# Approach-2:
# I have used slow-fast pointer approach
# put both pointer at head in starting
# while fast != none and fast.next!= none - one condn for even & one for odd length
# move slow by 1 and fast by 2
# at the end slow will be at the mid elem.
# so return slow


# Time Complexity : O(n)
# Space Complexity : O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None:
            return head
        
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        