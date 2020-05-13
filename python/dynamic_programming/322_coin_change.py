__author__ = 'zhangsensen'

'''
零钱兑换 Coin Change
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

解法：动态规划
p[i]表示金额为i时最少硬币个数，则对于coins中不大于i的硬币都可以作为一种选择
p[i] = min(p[i-coin] + 1) for coin in coins
'''


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    min_coin = min(coins)
    p = [float("inf")] * (amount + 1)
    p[0] = 0
    for i in range(min_coin, amount + 1):
        for coin in coins:
            if i >= coin and p[i - coin] < float("inf"):
                p[i] = min(p[i], p[i - coin] + 1)
    return p[amount] if p[amount] < float("inf") else -1


def coinChange2(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    min_coin = min(coins)
    p = [float("inf")] * (amount + 1)
    p[0] = 0
    for i in range(min_coin, amount + 1):
        for coin in coins:
            if i >= coin and p[i - coin] < float("inf"):
                p[i] = min(p[i], p[i - coin] + 1)
    return p[amount] if p[amount] < float("inf") else -1


def coinChange3(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    p = [float("inf")] * (amount + 1)


    return p[amount] if p[amount] < float("inf") else -1

if __name__ == '__main__':
    c = [1,2,5]
    a = 11
    r = coinChange(c, a)
    print(r)

