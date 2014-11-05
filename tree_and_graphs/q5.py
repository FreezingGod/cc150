class Solution:
    def checkBST(self, root):
        return self.myCheckBST(root, [-10e10])
    def myCheckBST(self, root, last):
        if not root: return True
        if !self.myCheckBST(root.left, last): return False
        if root.val <= last[0]: return False
        last[0] = root.val
        if !self.myCheckBST(root.right, last): return False
        return True

class Solution2:
    def checkBST(self, root):
        return self.myCheckBST(root, -10e10, 10e10)
    def myCheckBST(self, root, min, max):
        if not root: return True
        if root.val <= min or root.val > max:
            return False
        if !self.myCheckBST(root.left, min, root.val) or !self.myCheckBST(root.right, root.val, max):
            return False
        return True
