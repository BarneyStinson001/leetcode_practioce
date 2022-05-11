#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution():
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n!=0: #(n==0直接返回nums1)
            # 1、如果a空
            if m==0:
                nums1[:]=nums2[:]
            #初始化和比较
            else:
                i=-1-n
                j=-1
                idx=-1 
                # while (i>-m-n or j>-n):   
                while True:   
                    # if(nums1[i]>nums2[j]):#应该用倒序,先搞定nums后面空的位置。
                    if(nums1[i]<=nums2[j]): # 优先清空nums2
                        nums1[idx]=nums2[j]
                        j-=1
                        idx-=1
                        if j==-1-n:
                            break
                    else:
                        nums1[idx]=nums1[i]
                        i-=1
                        idx-=1
                        if i==-1-m-n:
                            break
                # 最后出来
                if(i!=-1-m-n and j==-1-n):
                    nums1[-m-n:idx+1]=nums1[0:m+n+idx+1]
                else:
                    nums1[-m-n:idx+1]=nums2[0:m+n+idx+1]  

        
        
# @lc code=end

if __name__=='__main__':
    sol=Solution()
    # nums=[1,2,3,0,0,0]
    # nums2=[1,1,3]
    nums=[2,0]
    nums2=[1]
    
    sol.merge(nums,len(nums)-len(nums2),nums2,len(nums2))
    print(nums)