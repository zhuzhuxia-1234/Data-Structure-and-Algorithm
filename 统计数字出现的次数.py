# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:11:31 2019

@author: zhuxibing
"""

###统计一个列表中数字出现的次数

##方法1 使用collections模块
from collections import Counter

def count_number(array):
    n=Counter(array)
    return n
##方法2 不使用外部模块
def count_number_1(array):
    result={}
    for num in array:
        if num not in result:
            result[num]=1
        else:
            result[num] +=1
    return result

if __name__=='__main__':
    array=[12,13,10,12,17,13,12]
    print(count_number(array))
    print(count_number_1(array))