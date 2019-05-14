# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:47:47 2019

@author: zhuxibing
"""


"""
动态规划求最大子序列的算法与分析(python描述)

体来说，假设数组为a[i]，因为最大连续的子序列和必须是在位置0-(n-1)之间的某个位置结束。那么，当循环遍历到第i个位置时，
如果其前面的连续子序列和小于等于0，那么以位置i结尾的最大连续子序列和就是第i个位置的值即a[i]。如果其前面的连续子序列和大于0，
则以位置i结尾的最大连续子序列和为b[i] = max{ b[i-1]+a[i]，a[i]}，其中b[i]就是指最大连续子序列的和。
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