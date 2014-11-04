class Solution:
    def deleteNode(n):
        if not n or not n.next:
            return False
        next = n.next
        n.data = next.data
        n.next = next.next
        return True
