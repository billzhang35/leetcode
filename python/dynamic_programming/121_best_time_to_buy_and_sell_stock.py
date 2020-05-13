__author__ = 'zhangsensen'

'''
买卖股票的最佳时机 Best Time to Buy and Sell Stock
给定表示股票价格的数组，求能取得的最大收益，要求只能买卖一次

解法一：遍历数组，一边更新最小价格，一边更新最大收益
复杂度：时间复杂度O(n)，空间复杂度O(1)

解法二：动态规划
存储：数组r[i][j], 表示第i天过后，当前是否持有股票（持有为1否则为0）时的最大收益
解析：题目要求只能买卖一次，因此只考虑每天持有或不持有的情况
初始值：r[i][j] = 0, r[0][1]= -prices[0]
递推式：r[i][0] = max(r[i-1][0], r[i-1][1] + prices[j])  当前不持有 = max(前一天不持有，今天卖出)
       r[i][1] = max(r[i-1][1], -prices[j])  当前持有 = max(前一天持有，今天买入)  注：今天买入说明之前没有买卖
输出：r[n - 1][0]  一定是不持有的时候收益最大
复杂度：时间复杂度O(n)，空间复杂度O(n)
'''


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, n):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit


def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    r = [[0] * 2 for i in range(n)]
    r[0][1] = -prices[0]
    for i in range(1, n):
        r[i][0] = max(r[i - 1][0], r[i - 1][1] + prices[i])
        r[i][1] = max(r[i - 1][1], -prices[i])
    print(r)
    return r[n - 1][0]


if __name__ == '__main__':
    a = [10, 9, 2, 5, 3, 7, 10, 8]
    #a = [5, 4, 3]
    #a = [3, 1, 8, 4]
    res = maxProfit2(a)
    print(res)
