# Definition for singly-linked list.
import random


# THIS PROBLEM STATEMENT MAKES NO FUCKING SENSE.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def __init__(self, head: ListNode): #Annotation :ListNode means head has to be of type ListNode
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getLinkedListLength(self):
        current_node = self.head
        list_length = 0
        while current_node:
            list_length+=1
            current_node = current_node.next
        return list_length

    def getRandom(self):
        """
        :rtype: int
        """
        list_length = self.getLinkedListLength()
        rand = random.randint(0, list_length)
        count = 0
        current_node = self.head
        while current_node:
            if count == rand:
                return current_node.val
            count+=1
            current_node = current_node.next










# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()