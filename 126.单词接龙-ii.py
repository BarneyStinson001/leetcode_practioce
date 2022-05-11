#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from inspect import iscoroutine
from queue import Queue


class Solution():
    def is_ok(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        if(str1[0]!=str2[0]):
            return str1[1:]==str2[1:]
        if(str1[-1]!=str2[-1]):
            return str1[:-1]==str2[:-1]
        if(len(str1)>=3):
            for i in range(1,len(str1)-1):
                if(str1[i]!=str2[i]):
                    return str1[0:i]==str2[0:i] and str1[i+1:]==str2[i+1:]
    
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        '''
        v0:
        判断相邻的函数
        BFS：
        找出wordList中和beginWord相邻的单词，标记visited为父亲节点beginWord,加入队列：
        队列不空：
            去队列首个元素判断是不是和endWord相邻。是的话 break return路径
            不是的话，把剩下的相邻的单词加入队列，标记visited为当前的word作为parentword。
        队列空了，也没匹配就直接返回
        所有最短路径： 这一层都要查完
        
        
        v1:生成路径，看最后一个和终点连不连通
        '''
        
        if len(beginWord)==1:
            return [beginWord,endWord]
        l=len(wordList)
        visited=[0 for i in range(l)]
        # 初始化路径        
        inital_path=[beginWord]
        #初始化所有可能的路径
        possibleways=[inital_path]
        res=[]
        while True:
            for way in possibleways:
                if self.is_ok(way[-1],endWord):#试探是否连通，如果连通，就是最短路径了
                    one_way=way[:]
                    one_way.append(endWord)
                    res.append(one_way)
                    #要所有最短路径，所以不要break提前退出
            #循环退出后再判断是否结束和返回
            if res:
                return res
            else:
                #还没最短路径，就延长一步。再进行循环试探
                all_poosible_way=[]
                for way in possibleways:
                    for i in range(l):
                        way_ori_tmp=way[:]
                        if (visited[i]==0) and self.is_ok(wordList[i],way[-1]):
                            #找出未visited，并和末枝相连的节点
                            way_ori_tmp.append(wordList[i])#更新可能的路径
                            visited[i]=1
                            all_poosible_way.append(way_ori_tmp)#保存
                            # print(all_poosible_way)
                if all_poosible_way:
                    possibleways=all_poosible_way  #继续循环进行
                else:
                    return []#如果未返回res,且已经不能延伸了，就返回[],表示失败
        
# @lc code=end

if __name__=='__main__':
    sol=Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    paths=sol.findLadders(beginWord,endWord,wordList)
    print(f"返回{paths}")