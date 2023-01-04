#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start


from operator import index
from time import time


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
        if endWord not in wordList:
            return []
        if len(beginWord)==1:
            return [[beginWord,endWord]]
        l=len(wordList)
        # visited，每次都是跟着way初始化
        # visited=[0 for i in range(l)]
        # 初始化路径        
        inital_path=[beginWord]
        #剪枝：
        # if beginWord in wordList:
        #     wordList.remove(beginWord)
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
                        visited=[0 for i in range(l)]
                        for node in way:
                            if node in wordList:
                                visited[wordList.index(node)]=1
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
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log","cog"]
    # paths=sol.findLadders(beginWord,endWord,wordList)
    # print(f"返回{paths}")

# 1、未解决
# "red"
# "tax"
# ["ted","tex","red","tax","tad","den","rex","pee"]
# 上一层多个节点可以到下一层的同一个节点

#2、超时
    t=time()
    print()
    beginWord = "cet"
    endWord = "ism"
    wordList =  ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    paths=sol.findLadders(beginWord,endWord,wordList)
    print(f"返回{paths}")
    print(time()-t1)
# 估计还得反向匹配一下