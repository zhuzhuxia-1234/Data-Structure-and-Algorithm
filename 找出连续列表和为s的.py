# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:55:59 2019

@author: zhuxibing
"""

def sum_to_s(s):
    a, b = 1, 2
    ret = []
    while a < s / 2 + 1:
        if sum(range(a, b+1)) == s:
            ret.append(range(a, b+1))
            a += 1
        elif sum(range(a, b+1)) < s:
            b += 1
        else:
            a += 1
    return ret

if __name__ == '__main__':
    test = 45
    print(sum_to_s(test))