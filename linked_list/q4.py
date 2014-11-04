class Solution:
    def partition(head, x):
        if not head: return None
        d1 = ListNode(0)
        d2 = ListNode(0)
        e1, e2 = d1, d2
        p = head
        while p:
            if p.val < x:
                e1.next = p
                e1 = e1.next
            else:
                e2.next = p
                e2 = e2.next
            p = p.next
        e1.next = d2.next
        return d1.next
