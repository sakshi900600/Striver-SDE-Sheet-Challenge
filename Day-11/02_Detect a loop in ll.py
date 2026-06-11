# Cycle Detection in ll:


# Approach: slow-fast pointer
# start both at head
# while either fast or fast.next not null:
# move slow 1 step and fast 2 step forward
# if slow ==fast then return true
# otherwise at the end return false from the fun.

# bc: if 0 or 1 node in ll then return false

# T.C = O(n)
# S.C = O(1)



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        

        return False

        