__author__ = 'zhangsensen'

'''
最大子序和 Maximum Subarray
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

解法：动态规划
设ms(i)为数组a以第i个元素为结尾的子序列和，则ms[i] = a[i] + max(0, ms[i-1])，找到最大的ms[i]
前面的子序列和如果为负则重新开始
'''


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 1:
        return 0
    max_sum = nums[0]
    last_sum = nums[0]
    for i in range(1, n):
        temp_sum = nums[i] + max(0, last_sum)
        max_sum = max(max_sum, temp_sum)
        last_sum = temp_sum
    return max_sum


if __name__ == '__main__':
    a = [-2,1,-3,4,-1,2,1,-5,4]
    a = [-2]
    r = maxSubArray(a)
    print(r)

