__author__ = 'zhangsensen'

'''
买卖股票的最佳时机4 Best Time to Buy and Sell Stock IV
给定表示股票价格的数组，求能取得的最大收益，要求最多可以买卖k次

峰谷法不适用，可能性较多，复杂度同动态规划

解法：动态规划
存储：数组r[i][j][k], 表示第i天过后，买过j次股票后，当前是否持有股票（持有为1否则为0）时的最大收益
      本题中，j = {0,1,2}
初始值：r[i][0][0] = 0, r[i][0][1] = -Infinity
        r[0][j][0] = -Infinity, j=1,...,k
        r[0][1][1] = -prices[0]
递推式：r[i][j][0] = max(r[i-1][j][0], r[i-1][j][1] + prices[j])  买过j次当前不持有 = max(昨天不持有状态不变，今天卖出)
        r[i][j][1] = max(r[i-1][j][1], r[i-1][j-1][0] - prices[j])  买过j次当前持有 = max(昨天持有不变，买过j-1次今天买入)
输出：max(r[n][j][0])
复杂度：时间复杂度O(n*k)，空间复杂度O(n)
'''


def maxProfit(k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2 or k < 1:
        return 0
    if k > n:
        return maxProfitInf(prices)
    # 此处只给第0行和第0列初始值即可
    r = [[[0, -float("inf")] for i in range(k + 1)] for j in range(n)]
    for i in range(1, k + 1):
        r[0][i][0] = -float("inf")
    r[0][1][1] = -prices[0]
    for i in range(1, n):
        for j in range(1, k + 1):
            r[i][j][0] = max(r[i - 1][j][0], r[i - 1][j][1] + prices[i])
            r[i][j][1] = max(r[i - 1][j][1], r[i - 1][j - 1][0] - prices[i])
    print(r)
    return max([x[0] for x in r[n - 1]])


def maxProfitInf(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    max_profit = 0
    temp_min, temp_max = prices[0], prices[0]
    for i in range(1, n):
        if prices[i] > temp_max:
            temp_max = prices[i]
        else:
            max_profit += temp_max - temp_min
            temp_min, temp_max = prices[i], prices[i]
    max_profit += temp_max - temp_min
    return max_profit


if __name__ == '__main__':
    a = [10, 9, 2, 5, 3, 7, 10, 8]
    a = [2, 1,4]
    #a = [3,3,5,0,0,3,1,4]
    a=[1,2,4,2,5,7,2,4,9,0]
    a = [1,2]
    #a=[6,1,3,2,4,7]
    a=[8,6,4,3,3,2,3,5,8,3,8,2,6]
    a=[1,2,4,2,5,7,2,4,9,0,9]
    #res1 = maxProfitByOneTime(a[2:7])[0]
    #print(res1)

    res = maxProfit(3, a)
    print(a)
    print(res)

