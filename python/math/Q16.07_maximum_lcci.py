__author__ = 'zhangsensen'

'''
编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
思路：两数互相表示的类型。max(a,b)=((a+b) + |a+b|)/2, min(a,b)=((a+b) - |a+b|)/2
'''


def maximum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    return ((a + b) + abs(a - b)) / 2


if __name__ == '__main__':
    r = maximum(3, 5)
    print(r)

