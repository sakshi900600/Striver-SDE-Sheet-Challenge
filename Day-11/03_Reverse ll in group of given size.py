# Reverse ll in group of given size:


# Approach:
# Everytime find kth node, store nextn and reverse k groups
# maintain a prev var and using it connect the reversed groups

# T.C = O(n)
# S.C = O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None or k==1:
            return head
        
        temp = head
        prev = None

        while temp != None:
            kthn = self.getKthNode(temp,k)

            if kthn == None:
                if prev == None:
                    break
                else:
                    prev.next = temp
                    break
            else:
                nextn = kthn.next
                kthn.next = None
                self.reverse(temp)

                if temp == head:
                    head = kthn
                
                if prev == None:
                    prev = temp
                else:
                    prev.next = kthn
                    prev = temp
            
                temp = nextn
        

        return head
    

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


    def getKthNode(self, head, k):
        temp = head
        cnt = 1

        while temp != None and cnt != k:
            temp = temp.next
            cnt += 1
        
        return temp
        