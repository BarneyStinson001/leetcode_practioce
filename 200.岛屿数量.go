/*
 * @lc app=leetcode.cn id=200 lang=golang
 *
 * [200] 岛屿数量
 */

// @lc code=start
package main
func numIslands(grid [][]byte) int {
    
    m:=len(grid)
    n:=len(grid[0])

    //初始化:各自为营
    root :=make([]int,m*n)
    for i:=0;i<m*n;i++{
        root[i]=i
    }

    //并查操作
    for i:=0;i<m;i++{
        for j:=0;j<n;j++{
            if grid[i][j]==1{
                //如果是1，再检查周围的有没有1，有1就合并
                if i+1<m&&grid[i+1][j]==1{
                    UnionSet(root,n*i+j,n*(i+1)+j)
                }
                if j+1<n&&grid[i][j+1]==1{
                    UnionSet(root,n*i+j,n*i+j+1)
                } 

            }    
        }
    }

    //返回结果
    res :=0
    for i:=0;i<m*n;i++{
        if grid[i/n][i%n]==1 && FindRoot(root,i)==i{
            res++
        }
    }

    return res
}




//并查集函数：并
func UnionSet(fa []int,x int,y int){
    x,y=FindRoot(fa,x),FindRoot(fa,y)
    if x!=y{
        fa[y]=x
    }
}

//并查集函数：查
func FindRoot(fa []int,x int) int{
    if (fa[x]==x) {return x}
    fa[x]=FindRoot(fa,fa[x])
    return fa[x]
}



func main() {		
	test = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
	fmt.Printf(numIslands(test))
}


// @lc code=end

