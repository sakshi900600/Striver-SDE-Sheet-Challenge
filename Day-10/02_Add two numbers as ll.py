# Add two numbers as ll:


# Approach:
# here the number and results both are given already reversed, so don't need to reverse anything
# take 2 pointer for both list.
# create dummy node and take a temp pointer for it.
# take carry = 0
# while any of list exists: add values and create newNode add in temp 
# update the carry and continue
# at the end check if still some carry left, then create a newNode from that and update it.

# return the dummy.next as our new head

# T.C = O(n+m)
# S.C = O(n+m)



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)

        t1 = l1
        t2 = l2
        temp = dummy

        carry = 0

        while t1 or t2:
            data = carry
            if t1:
                data += t1.val
                t1 = t1.next
            if t2:
                data += t2.val
                t2 = t2.next
            
            newNode = ListNode(data % 10)
            temp.next = newNode
            temp = newNode

            carry = data // 10
        

        while carry:
            newNode = ListNode(carry % 10)
            temp.next = newNode
            temp = newNode

            carry = carry // 10
        
        return dummy.next

              