# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListAndRemoveDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        data_appearances = {}
        current_node, previous_node = head, None
        while current_node is not None:
            if current_node.val in data_appearances:
                data_appearances[current_node.val] = int(data_appearances[current_node.val]) + 1
            else:
                data_appearances[current_node.val] = 1
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        head = previous_node

        current_node, previous_node = head, None
        while current_node is not None:
            if data_appearances[current_node.val] > 1:
                if previous_node is None:
                    head = current_node.next
                    current_node.next = None
                    current_node = head
                else:
                    previous_node.next = current_node.next
                    current_node = current_node.next
            else:
                previous_node = current_node
                current_node = current_node.next
        return head

