__author__ = 'zhangsensen'

'''
不同路径 Unique Paths
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？


解法：动态规划
p[i][j]表示从起点到位置(i, j)的不同路径的数量
根据机器人只能向下或向右移动一步，(i,j)的上个状态只能是(i-1,j)或(i,j-1)
p[i][j] = p[i-1][j] + p[i][j-1] 

'''


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    p = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 1 or j == 1:
                p[i][j] = 1
            else:
                p[i][j] = p[i - 1][j] + p[i][j - 1]
    return p[m][n]

def uniquePaths2(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    p = [[1] * n for i in range(2)]
    for i in range(1, m):
        for j in range(1, n):
            p[1][j] = p[0][j] + p[1][j - 1]
        p[0] = p[1][:]
    return p[1][n-1]

if __name__ == '__main__':
    r = uniquePaths2(7, 3)
    print(r)

