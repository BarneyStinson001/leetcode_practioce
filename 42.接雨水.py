#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#  left_tmp  peak  right_tmp

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        # 找到最大值max，以max_index为界，左边区间从左边开始向右遍历；右边区间从右边往左遍历，
        count = 0
        
        # 找出最大峰
        peak = height[0]
        peak_index = 0
        for i in range(len(height)):
            if height[i]>peak:
                peak = height[i]
                peak_index = i
        
        # 计算左边的水
        left_tmp=height[0]
        i=1
        while(i<peak_index):
            if(height[i]>left_tmp):
                left_tmp=height[i]
            else:
                count += left_tmp-height[i]
            i+=1
        
        # 计算右边的水
        right_tmp=height[-1]
        i=-2
        while(i>peak_index-len(height)):
            if(height[i]>right_tmp):
                right_tmp=height[i]
            else:
                count += right_tmp-height[i]
            i-=1
        
        return count
            
        
        
# @lc code=end

if __name__ =='__main__':
    input=[4,2,3]
    print(Solution.trap(height=input))