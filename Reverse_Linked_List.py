# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        prev_node = None
        while current_node is not None:
            next_node = current_node.next  # Remember next node
            current_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = current_node  # Used in the next iteration.
            current_node = next_node  # Move to next node.
        head = prev_node
        return head
