# https://www.acmicpc.net/problem/10826
import sys


def fibonacci(num: int):
    '''
    With Memoization

    @param num: An integer number in range [0, 10000]
    '''

    memo = dict([(0, 0), (1, 1)])

    def helper(num: int):
        if num in memo:
            return memo[num]

        memo[num] = helper(num-1) + helper(num-2)
        return memo[num]

    return helper(num)


sys.setrecursionlimit(10050)
print(fibonacci(int(input())))
