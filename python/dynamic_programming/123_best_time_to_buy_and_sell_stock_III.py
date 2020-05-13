__author__ = 'zhangsensen'

'''
买卖股票的最佳时机3 Best Time to Buy and Sell Stock III
给定表示股票价格的数组，求能取得的最大收益，要求最多可以买卖两次

解法一：峰谷法。
最多交易1次：找最大的上升段
最多交易无限次：找所有的上升段
最多交易x次：找到最大的x个不重叠的上升段
1) 由prices差值的到差值数组，去掉0，合并相邻的同号项
2) 把正项和负项分别降序排序，得到数组pos和neg
4) 从第x+1项开始，得到comp数组，comp[i]=pos[x+1+i]-neg[i]，取出正项
5) 最大收益为pos前x项和 + comp所有正项之和
复杂度：时间复杂度O(n)，空间复杂度O(1)

解法二：动态规划
存储：数组r[i][j][k], 表示第i天过后，买过j次股票后，当前是否持有股票（持有为1否则为0）时的最大收益
      本题中，j = {0,1,2}
初始值：r[i][0][0] = 0, r[i][0][1] = -Infinity
        r[0][1][0] = -Infinity, r[0][1][1] = -prices[0]
        r[0][2][0] = -Infinity, r[0][2][1] = -Infinity
递推式：r[i][j][0] = max(r[i-1][j][0], r[i-1][j][1] + prices[j])  买过j次当前不持有 = max(昨天不持有状态不变，今天卖出)
        r[i][j][1] = max(r[i-1][j][1], r[i-1][j-1][0] - prices[j])  买过j次当前持有 = max(昨天持有不变，买过j-1次今天买入)
输出：max(r[n][j][0])
复杂度：时间复杂度O(n*k)，空间复杂度O(n)
'''


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    max_times = 2
    profits = [0] * (n - 1)
    for i in range(0, n - 1):
        profits[i] = prices[i + 1] - prices[i]
    profits = [_ for _ in profits if _ != 0]
    if len(profits) < 1:
        return 0

    cont_profits = []
    temp_sum = profits[0]
    for i in range(1, len(profits)):
        if profits[i] * profits[i - 1] > 0:
            temp_sum += profits[i]
        else:
            cont_profits.append(temp_sum)
            temp_sum = profits[i]
    cont_profits.append(temp_sum)

    if len(cont_profits) < 2:
        return max(0, cont_profits[0])
    if cont_profits[0] < 0:
        cont_profits = cont_profits[1:]
    if cont_profits[-1] < 0:
        cont_profits = cont_profits[:-1]

    positives = sorted([_ for _ in cont_profits if _ > 0], reverse=True)
    negatives = sorted([_ for _ in cont_profits if _ < 0], reverse=True)
    if len(positives) <= max_times:
        max_profit = sum(positives)
    else:
        len_comp = min(len(positives) - max_times, len(negatives))
        comp = [0] * len_comp
        for i in range(0, len_comp):
            comp[i] = positives[i + max_times] + negatives[i]
        max_profit = sum(positives[:max_times]) + sum(_ for _ in comp if _ > 0)
    return max_profit


def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    max_times = 2
    # 此处只给第0行和第0列初始值即可
    r = [[[0, -float("inf")] for i in range(max_times + 1)] for j in range(n)]
    r[0][1][0], r[0][2][0] = -float("inf"), -float("inf")
    r[0][1][1] = -prices[0]
    for i in range(1, n):
        for j in range(1, max_times + 1):
            r[i][j][0] = max(r[i - 1][j][0], r[i - 1][j][1] + prices[i])
            r[i][j][1] = max(r[i - 1][j][1], r[i - 1][j - 1][0] - prices[i])
    print(r)
    return max([x[0] for x in r[n - 1]])


if __name__ == '__main__':
    a = [10, 9, 2, 5, 3, 7, 10, 8]
    #a = [3,3,5,0,0,3,1,4]
    a=[1,2,4,2,5,7,2,4,9,0]
    a=[8,6,4,3,3,2,3,5,8,3,8,2,6]
    a=[1,2,4,2,5,7,2,4,9,0,9]
    #res1 = maxProfitByOneTime(a[2:7])[0]
    #print(res1)

    res = maxProfit(a)
    print(a)
    print(res)
