__author__ = 'zhangsensen'

'''
最长上升子数列 Longest Increasing Subsequence
解法：动态规划
存储：数组lis[i], 表示包含第i个元素的前i个元素的最大上升子数列长度
初始值：lis[i] = 0, i = 0...n-1
递推式：lis[i] = max(lis[j]) + 1, if nums[i]>nums[j], j=0...i-1
输出：max(dp)
复杂度：时间复杂度O(n^2)，空间复杂度O(n)
'''


def lengthOfLIS(nums):
    n = len(nums)
    if n <= 0:
        return 0
    lis = [1] * n
    for i in range(1, n):
        temp_lis = 0
        for j in range(0, i):
            if nums[i] > nums[j]:
                temp_lis = max(temp_lis, lis[j])
        lis[i] = temp_lis + 1
    return max(lis)


if __name__ == '__main__':
    a = [10, 9, 2, 5, 3, 7, 101, 18]
    res = lengthOfLIS(a)
    print(res)

