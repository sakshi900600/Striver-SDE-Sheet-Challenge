# Check if ll is palindrome or not.

# Approach:
# Got the mid of ll using slow-fast
# reverse the second half slow to null
# compare first head, 2nd rev head data 
# if not matching anywhere return false
# otherwise return true

# T.C = O(n)
# S.C = O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        h1 = head
        h2 = self.reverse(slow)

        while h2 != None:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        

        return True
    
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        
        curr = head
        prev = None

        while curr != None:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        
        return prev




        