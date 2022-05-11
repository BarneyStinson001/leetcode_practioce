#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        '''
        [1,2,2] 2*3
        [],[1]    1可取可不取
        [],[2],[2,2]  2可取 0,1,2个，再排列组合
        '''
        #1、统计元素出现的个数
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        res=[]
        
        # 1、开始排列组合
        for k,v in dict.items():
            # 2、得到这个元素的排列组合tmp，[] [1] [1,1] ……
            tmp1=[[],[k]]
            if v>1:
                for i in range(1,v):
                    for ele in tmp1:
                        ele.append(k)
                    tmp1.append([])
            # print(tmp1)
            #3、 和历史的res进行组合
            # res=[[],[1]]
            # tmp=[[],[2],[2,2]]   
            #如果是第一个key，res=[]，在else赋值成tmp：
            if  res: 
                res_ori=res[:] #原始结果 其实就是和[]组合的结果
                # print(res_ori)
                res_tmp=[]
                for ele in tmp1:#[[],[2],[2,2] 
                    # print(ele)
                    # print(type(ele))
                    to_add_tmp=res_ori
                    # print(to_add_tmp)
                    if ele!=[]:  #下面分别与[2],[2,2组合]
                        for res_ele in to_add_tmp:#[[],[1]]  
                            res_ele=res_ele+ele#让to_add_tmp每个元素都加上ele[2]或[2,2]
                            # print(type(res_ele))
                            # print(res_tmp)  #改元素res_ele没改到res_tmp
                            res_tmp.append(res_ele) #一次循环个数加一遍。即生成v-1倍        
                res=res+res_tmp
            else:
                res=tmp1
                # print(res)
        return res
        
        
# @lc code=end
if __name__=='__main__':
    sol=Solution()
    input=[1]
    input=[1,1]
    input=[1,1,1]
    input=[1,2,2]
    print(sol.subsetsWithDup(input))
    
    
