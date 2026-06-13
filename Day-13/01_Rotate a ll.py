# 61. Rotate List

# Approach:
# Here first i find out tail and length of ll.
# Then take modulo of k = k%length
# Then reach at the length-k-1 nth node and stored its next node as newhead
# changed the links and returned newhead


# T.C = O(n)
# S.C = O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None or head.next==None or k==0:
            return head

        length = 0
        temp = head
        tail = None

        while temp != None:
            tail = temp
            length += 1
            temp = temp.next 
        
        k = k % length
        if k == 0:
            return head
            
        temp = head
        cnt = length - k-1
        while temp != None and cnt > 0:
            cnt -= 1
            temp = temp.next
        
        new_head = temp.next
        temp.next = None
        tail.next = head

        return new_head
        