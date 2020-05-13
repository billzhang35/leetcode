__author__ = 'zhangsensen'

'''
最长回文子串 Longest Palindromic Substring
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

解法一：动态规划
p[i, j]表示从string的第i个字符到第j个字符的子串是否回文
p[i, j] = p[i+1, j-1] and s[i]==s[j]
p[i, i] = 1, p[i, i+1] = I(p[i]==p[i+1])
遍历顺序：从二维矩阵对角线分别向右上计算
复杂度：O(n^2)
'''


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    p = [[False] * n for i in range(n)]
    max_len = 0
    start = 0
    end = 0
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
            if diff > max_len and p[i][j]:
                start = i
                end = j
                max_len = diff
    return s[start: end + 1]


if __name__ == '__main__':
    a = "babad"
    a = "cbbd"
    a = "dabba"
    r = longestPalindrome(a)
    print(r)

