# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:36:56 2019

@author: dell
"""

class Solution:
    def ReverseSentence(self, s):
        # write code here
        l=s.split(" ")
        print(l)
        return " ".join(l[::-1])
print(Solution().ReverseSentence("student a am I"))

