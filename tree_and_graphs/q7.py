class Solution:
# assume p and q are nodes in tree rooted at root
    def commonAncestor(self, root, p, q):
        if p == q:
            return p
        else:
            return self.commonAncestorHelper(root, p, q)
    def commonAncestorHelper(self, root, p, q):
        if not root: return None
        if root == p or root == q:
            return root
        x = self.commonAncestorHelper(root.left, p, q)
        if x and x != p and x != q:
            return x
        y = self.commonAncestorHelper(root.right, p, q)
        if y and y != p and y != q:
            return y
        if x and y:
            return root
        else:
            return x if x else y


class Solution2:
# does not know if p and q are in the tree rooted at root
    def commonAncestor(self, root, p, q):
        return self.commonAncestorHelper()[1]
    def commonAncestorHelper(self, root, p, q):
        if not root: return (None, False)
        if root == p and root == q:
            return (root, True)
        x = self.commonAncestorHelper(root.left, p, q)
        if x[1]:
            return x
        y = self.commonAncestorHelper(root.right, p, q)
        if y[1]:
            return y
        if x[0] and y[0]:
            return (root, True)
        elif root == p or root == q:
            if x[0] or y[0]:
                return (root, True)
        else:
            if x[0]:
                return (x[0], False)
            elif y[0]:
                return (y[0], False)
            else:
                return (None, False)

