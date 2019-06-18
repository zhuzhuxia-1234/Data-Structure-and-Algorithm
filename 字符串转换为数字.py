# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:03:36 2019

@author: dell
"""

class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        ret = 0
        num = 0
        fuhao = 1
        for i in s[::-1]:
            if i < '0' or i > '9':
                if i == '-':
                    fuhao = -1
                    continue
                elif i == '+':
                    continue
                else:
                    return 0
            ret += int(i) * pow(10, num)
            num += 1
        return ret*fuhao
    
    def str_to_int(self,s):
        try:
            return int(s)
        except:
            return 0
print(Solution().StrToInt("123"))
print(Solution().str_to_int("123"))

