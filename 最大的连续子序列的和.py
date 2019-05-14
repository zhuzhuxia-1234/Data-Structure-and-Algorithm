# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:47:47 2019

@author: zhuxibing
"""


"""
动态规划求最大子序列的算法与分析(python描述)
首先寻找最优子问题,[-2,1,-3,4,-1,2,1,-5,4],第一个最优子问题为-2,那么到下一个1时,其最优为当前值或者当前值加上上一个最优值,因而可以得到其递推公式
dp[i] = max(nums[i], nums[i] + dp[i - 1])


"""





class solution():
    def FindGreatestSumOfSubArray(self, nums):
        l = len(nums)
        i = 0
        sum = 0
        MaxSum = nums[0]
        while i < l:
            sum+=nums[i]
            print(sum)
            if sum > MaxSum:
                MaxSum = sum
            if sum < 0:
                sum = 0
            i+=1
        return MaxSum

if __name__=='__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    print(solution().FindGreatestSumOfSubArray(nums))
