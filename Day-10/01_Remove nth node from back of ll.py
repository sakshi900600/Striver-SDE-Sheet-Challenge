# Remove nth node from back of ll:


# Approach:
# find out length of the ll.
# reach at one node before the node which we have to delete.
# point this prev nodes next to node to be deleted next.
# return head

# sc: if we have to delete head lenght-n==0 then update the head as head.next

# T.C = O(n)
# S.C = O(1)


# Approach: slow-fast to delete in single pass
# First create a dummy node and attatch it with head
# take slow,fast at dummy
# first move fast to n steps
# after that until fast != None: move both slow,fast
# now slow will be pointing to the prev node, from the node which we have to delete
# connect slow.next to slow.next.next
# return dummy.next as the head




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        cnt = 0
        temp = head
        while temp != None:
            cnt += 1
            temp = temp.next
        
        ntdel = cnt - n

        if ntdel == 0:
            head = head.next
            return head
        
        cnt = 1
        temp = head

        while temp != None and cnt != ntdel:
            temp = temp.next
            cnt += 1
        
        temp.next = temp.next.next

        return head


    def removeNthFromEnd2(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n+1):
            fast = fast.next
        
        while fast != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next

        