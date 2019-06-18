# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:17:28 2019

@author: zhuxibing
"""
##如果一个数被质数2，3，5整除后余数是1，则该数是丑数
import time
def finduglynum(n):
	time.clock()
	uglynum = []
	i = 1
	count = 0
	while True:
		temp = i
		while temp%2 == 0:
			temp = temp//2
		while temp%3 == 0:
			temp = temp//3
		while temp%5 == 0:
			temp = temp//5
		if temp == 1:
			uglynum.append(i)
			count += 1
		if count >= n:
			break
		i += 1
	print("运行时间：", time.clock())
	print(uglynum)
	
def GetUglyNumber_Solution(self, index):
        # write code here
    if index<=0:
        return 0
    ugly_list=[1]
    indextwo=0
    indexthree=0
    indexfive=0
    for i in range(index-1):
        newugly=min(ugly_list[indextwo]*2,ugly_list[indexthree]*3,ugly_list[indexfive]*5)
        ugly_list.append(newugly)
        if newugly%2==0:
            indextwo+=1
        if newugly%3==0:
            indexthree+=1
        if newugly%5==0:
            indexfive+=1
    return ugly_list[-1]
# 测试
finduglynum(20)
