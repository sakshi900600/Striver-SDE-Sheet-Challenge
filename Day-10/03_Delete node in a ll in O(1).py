# Delete Node in a Linked List in O(1)

# In this ques, we are directly given the node not the head of ll and we have to delete this node in constant time.


# Approach:
# We can copy the data of its next node into it and 
# point this node's next to its next node's next.

# T.C = O(1)
# S.C = O(1)



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

        