# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:13:59 2019

@author: zhuxibing
"""

#斐波那契数列1 1 2 3 5 8 13 21 。。。。 求第n个数 使用递归实现

class solution():
    def Fibonacci(self,n):
        if n==1:
            return 1
        if n==2:
            return 1
        if n>=3:
            s=[]
            s.append(1)
            s.append(1)
            for i in range(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]

if __name__=="__main__":
    s=solution()
    print(s.Fibonacci(5))