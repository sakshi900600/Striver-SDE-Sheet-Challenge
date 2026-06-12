# Linked List Cycle II


# Approach:
# First checked if cycle exists or not using slow-fast pointer
# if not return none.
# otherwise again start slow at head and while both are not equal
# move both pointers 1 step
# return slow/fast coz both are at same node (loop starting point)

# T.C = O(n)
# S.C = O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head
        fast = head
        iscycle = False

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                iscycle = True
                break
        
        if not iscycle:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        