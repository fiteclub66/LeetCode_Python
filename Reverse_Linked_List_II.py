# UNFINISHED - Their solutions don't make any fucking sense


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return None

        current_node = head
        left_holder, right_holder = None, None
        while current_node is not None:
            if current_node.val == left:
                left_holder = current_node
                print("left_holder" + str(left_holder))
            if current_node.val == right:
                right_holder = current_node
                print("right_holder" + str(right_holder))
            current_node = current_node.next
        print("current state: " + str(head))

        current_node, previous_node = head, None
        while current_node is not None:
            if current_node.val == left:
                print("remapping left")
                previous_node.next = right_holder
                right_holder.next = left_holder.next
            if current_node.val == right:
                print("remapping right")
                current_node.next = left_holder.next
                previous_node.next = left_holder
                return head
            previous_node = current_node
            current_node = current_node.next
        return head



