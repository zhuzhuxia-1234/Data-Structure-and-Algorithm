# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:32:52 2019

@author: dell
"""

##在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        c={}
        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for index,i in enumerate(s):
            if c[i] is 1:
                return index
        return -1
    
    # 一行版本
    def FirstNotRepeatingChar_onerow(self, s):
        return s.index(list(filter(lambda x: s.count(x) == 1, s))[0]) if s else -1

if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('google'))
    print(Solution().FirstNotRepeatingChar_onerow("google"))
