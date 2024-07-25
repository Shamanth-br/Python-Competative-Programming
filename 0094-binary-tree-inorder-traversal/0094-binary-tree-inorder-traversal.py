# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        parent = root
        ans = []
        # if .left,.right == none It is leaf node
        # save previous root as top node is not stored
        # left,current,right so recursive 
        #if leaf node or current.left.val in ans and current.right.val in ans
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans
            
            