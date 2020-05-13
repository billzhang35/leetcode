__author__ = 'zhangsensen'

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转

思路：整数反转一类的问题，不要用字符串的方法，要从数字位数提取入手。
取出末位：d=x%10, x=x//10
取出首位：d=x//(10**math.floor(math.log10(x)))
对基本位运算要熟练
'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    BOUND = (1 << 31) - 1 if x > 0 else 1 << 31
    r = 0
    sign = 1 if x >= 0 else -1
    x = x * sign
    while x != 0:
        r = r * 10 + x % 10
        if r > BOUND:
            return 0
        x = x // 10
    return r * sign


if __name__ == '__main__':
    a = 1563847412
    res = reverse(a)
    print(res)
