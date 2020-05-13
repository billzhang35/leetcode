__author__ = 'zhangsensen'

'''
自除数 是指可以被它包含的每一位数除尽的数。自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
'''


def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    r = []
    for i in range(left, right + 1):
        flag = True
        num_i = i
        while num_i != 0:
            d = num_i % 10
            if d == 0 or i % d != 0:
                flag = False
                break
            num_i //= 10
        if flag: r.append(i)
    return r


def selfDividingNumbers2(left, right):
    r = []
    for i in range(left, right + 1):
        if '0' not in str(i) and all([i % int(_) == 0 for _ in str(i)]):
            r.append(i)
    return r

if __name__ == '__main__':
    res = selfDividingNumbers2(1, 22)
    print(res)
