#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution():
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method 1:计算个数，再赋值
        # count0=0
        # count1=0
        # for i in range(len(nums)):
        #     if(nums[i]==0):
        #         count0+=1
        #     if(nums[i]==1):
        #         count1+=1
        # for i in range(count0):
        #     nums[i]=0
        # for i in range(count0,count0+count1):
        #     nums[i]=1
        # for i in range(count0+count1,len(nums)):
        #     nums[i]=2
        
        # method 2 :多指针   
        # 0往头上，i+1 left+1
        # 2往尾巴上丢,right和i互换，不加i  
        # 如果是1,只+i  
        left=0
        right=-1
        i=0
        while(i<=len(nums)+right):
            if nums[i] == 0 :
                nums[left],nums[i]=nums[i],nums[left]
                i+=1
                left+=1
                continue
            if nums[i] == 2:
                nums[i],nums[right]=nums[right],nums[i]
                right -=1
                continue
            if nums[i] == 1:
                i+=1

# @lc code=end

if __name__=='__main__':
    sol=Solution()
    input=[2,0,1]
    print(sol.sortColors(input))