# Runtime: 83 ms, faster than 88.16% of Python online submissions for Add Two Numbers.
# Memory Usage: 13.7 MB, less than 91.96% of Python online submissions for Add Two Numbers.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_num_string = ""
        second_num_string = ""

        current_node = l1
        while current_node is not None:
            first_num_string = str(current_node.val) + first_num_string
            current_node = current_node.next

        current_node = l2
        while current_node is not None:
            second_num_string = str(current_node.val) + second_num_string
            current_node = current_node.next

        total_num_string = str(int(first_num_string) + int(second_num_string))

        head = None
        previous_node = None
        for i in range(len(total_num_string)):
            node = ListNode(int(total_num_string[i]), None)
            if previous_node is not None:
                node.next = previous_node
            previous_node = node
            if (i + 1) == len(total_num_string):
                head = node

        return head
