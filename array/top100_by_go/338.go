package main

import("fmt")
func countBits(n int) []int {
    res:=make([]int,1,n+1)//n=0直接初始化为0
    //与运算

    for i:=1;i<=n;i++{//从1开始；不能少了=
        res=append(res,count1(n))
    }
    return res
}

func count1(n int)int{
    res:=0
    for ;n>0;n&=n-1{
        res++
    }
    return res
}


func main()  {
	fmt.Println(countBits(3))
}