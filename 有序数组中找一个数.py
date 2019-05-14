# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:41:05 2019

@author: zhuxibing
"""

# 二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
# 从左下角（或右上角）开始遍历数组

def find_integer(matrix,num):
    if not matrix:
        return False
    rows,cols=len(matrix),len(matrix[0])
    row,col=rows-1,0
    while row>=0 and col<=cols-1:
        if matrix[row][col]==num:
            return True
        elif matrix[row][col]>num:
            row -=1
        else:
            col+=1
    return False

if __name__=='__main__':
    matrix=[[1,2,3],[2,4,6],[3,5,7],[5,7,11]]
    num=6
    print(find_integer(matrix,num))