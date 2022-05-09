#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution():
    def subsets(self, nums: list[int]) -> list[list[int]]:
        '''
        全排列，不知道是几重循环，递归
        '''
        # 递归终点,不对是从起点递推
        # if(len(nums)==1):
        #     return [[],[nums[0]]]
        
        # # 递归表达式，应该是递推表达式
        # if(len(nums)>1):
        #     return [[],[nums[0]],[subsets(nums[1:])],[nums[0],[subsets(nums[1:])]]]
        if len(nums)==1:
            return [[],[nums[0]]]
        else:
            res=[[],[nums[0]]]
            for i in range(1,len(nums)):
                tmp1=res
                tmp2=[]
                for ele in res:
                    tmp2.append(ele+[nums[i]])
                    # tmp2=res.append(nums[i])#应该是每个元素都加
                res=tmp1+tmp2     
        return res
             
        
# @lc code=end

if __name__=='__main__':
    sol=Solution()
    print(sol.subsets([1]))

