__author__ = 'zhangsensen'

'''
回文子串 Palindromic Substrings
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

解法一：动态规划
思路同5_longest_palindromic_substring，求最长改为求和
p[i, j]表示从string的第i个字符到第j个字符的子串是否回文
p[i, j] = p[i+1, j-1] and s[i]==s[j]
p[i, i] = 1, p[i, i+1] = I(p[i]==p[i+1])
遍历顺序：从二维矩阵对角线分别向右上计算
复杂度：O(n^2)
'''


def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    p = [[False] * n for i in range(n)]
    count = 0
    for diff in range(0, n):
        for i in range(0, n):
            j = i + diff
            if j > n - 1:
                continue
            if diff == 0:
                p[i][j] = True
            elif diff == 1:
                p[i][j] = s[i] == s[j]
            else:
                p[i][j] = p[i + 1][j - 1] and s[i] == s[j]
            count += p[i][j]
    return count


if __name__ == '__main__':
    a = "babad"
    a = "cbbd"
    a = "aaa"
    r = countSubstrings(a)
    print(r)

