# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:17:28 2019

@author: zhuxibing
"""

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
 
# 测试
finduglynum(20)
