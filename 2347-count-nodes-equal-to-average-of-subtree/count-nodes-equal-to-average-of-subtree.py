class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):

            if not node:
                return 0,0,0

            left_sum,left_count,left_matches = dfs(node.left)
            right_sum,right_count,right_matches = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            total_matches = left_matches + right_matches + (node.val == total_sum // total_count)

            return total_sum, total_count,total_matches

        return dfs(root)[2]