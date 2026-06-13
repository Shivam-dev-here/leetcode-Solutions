# Slow and Fast Techniqe

class Solution(object):
    def middleNode(self, head):

        current = head
        slow = head
        fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
        