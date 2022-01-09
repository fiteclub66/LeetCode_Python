#SUCCESS
#Runtime: 2184 ms, faster than 42.86% of Python online submissions for Remove Duplicates From an Unsorted Linked List.
#Memory Usage: 89.8 MB, less than 78.57% of Python online submissions for Remove Duplicates From an Unsorted Linked List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        current_node = head
        data_appearances = {}
        while current_node is not None:
            if current_node.val in data_appearances:
                data_appearances[current_node.val] = int(data_appearances[current_node.val]) + 1
            else:
                data_appearances[current_node.val] = 1
            current_node = current_node.next
        print(data_appearances)

        current_node, previous_node = head, None
        while current_node is not None:
            if data_appearances[current_node.val] > 1:
                if previous_node is None:
                    print(current_node.val)
                    current_node = current_node.next
                    head = current_node

                else:
                    previous_node.next = current_node.next
                    current_node = previous_node
            else:
                previous_node = current_node
                current_node = current_node.next
        return head