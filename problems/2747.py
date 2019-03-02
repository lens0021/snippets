# https://www.acmicpc.net/problem/2747


def fibonacci(num: int):
    '''
    With Memoization

    @param num: A Natural number in range [1, 45]
    '''

    memo = dict([(0, 0), (1, 1)])

    def helper(num: int):
        if num in memo:
            return memo[num]

        memo[num] = helper(num-1) + helper(num-2)
        return memo[num]

    return helper(num)


print(fibonacci(int(input())))
