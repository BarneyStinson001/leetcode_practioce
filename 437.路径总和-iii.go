/*
 * @lc app=leetcode.cn id=437 lang=golang
 *
 * [437] 路径总和 III
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) int {
	//所有排列组合 遍历后求值

	//遍历，递归利用定义

	if root == nil {
		return 0
	}
	if root.Val == targetSum {
		return 1
	}
	//经过root,等于从左右子树中找出等于target-root.Val的解
	left_use_left := pathSum(root.Left, targetSum-root.Val)
	right_use_right := pathSum(root.Right, targetSum-root.Val) //图中的5->2->1  ，以及解决不了5->2->1->0?

	//不经过root，那就直接递归调用 等于target的解
	left_not_use := pathSum(root.Left, targetSum)
	right_not_use := pathSum(root.Right, targetSum)

	return left_use_left + right_use_right + left_not_use + right_not_use
}

// @lc code=end

