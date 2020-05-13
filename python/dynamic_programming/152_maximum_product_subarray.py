__author__ = 'zhangsensen'

'''
乘积最大子序列 Maximum Product Subarray
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

解法：动态规划
p[i]以nums[i]结尾的非零子序列乘积，即遇到0则重新累乘
p[i] = p[i-1] * p[i] if p[i-1]!=0 else nums[i]
'''


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0: return 0
    max_product = -float("inf")
    p = nums[:]
    for i in range(1, n):
        p[i] = p[i - 1] * p[i] if p[i - 1] != 0 else nums[i]
        max_product = max(max_product, p[i])
    return max_product


if __name__ == '__main__':
    a = [2,3,-2,4]
    a = [-1,0,-2]
    a = [-2,-3,0,-4,1,-5,-2]
    r = maxProduct(a)
    print(r)

