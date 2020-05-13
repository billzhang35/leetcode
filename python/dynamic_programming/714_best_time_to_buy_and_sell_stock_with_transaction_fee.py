__author__ = 'zhangsensen'

'''
买卖股票的最佳时机(含手续费) Best Time to Buy and Sell Stock with Transaction Fee
给定表示股票价格的数组，求能取得的最大收益，要求可以买卖任意次，每次买卖有手续费

峰谷法是适用于遍历过程中可以即时结算的情况，多步规划比较过程复杂，不如动态规划

解法：动态规划
解析：思路与只能买卖一次相同，不同之处在于只能买卖一次的情况下，今日买入的收益为-prices[i]（买入前收益r[i-1][0]一定为0）
      买卖任意次的情况下，买入前收益r[i-1][0]不一定为0
存储：数组r[i][j], 表示第i天过后，当前是否持有股票（持有为1否则为0）时的最大收益
初始值：r[i][j] = 0, r[0][1]= -prices[0]-fee
递推式：r[i][0] = max(r[i-1][0], r[i-1][1] + prices[j])  当前不持有 = max(前一天不持有，今天卖出)
        r[i][1] = max(r[i-1][1], r[i-1][0] - prices[j] - fee)  当前持有 = max(前一天持有，今天买入) 
输出：r[n - 1][0]  一定是不持有的时候收益最大
复杂度：时间复杂度O(n)，空间复杂度O(n)
'''


def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    r = [[0] * 2 for i in range(n)]
    r[0][1] = -prices[0] - fee
    for i in range(1, n):
        r[i][0] = max(r[i - 1][0], r[i - 1][1] + prices[i])
        r[i][1] = max(r[i - 1][1], r[i - 1][0] - prices[i] - fee)
    print(r)
    return r[n - 1][0]


if __name__ == '__main__':
    a = [1, 3, 2, 8, 4, 9]
    #a = [5, 4, 3]
    #a = [3, 1, 8, 4, 5]
    res = maxProfit(a, 2)
    print(res)
