# https://www.acmicpc.net/problem/10870


def fibonacci(num: int):
    '''
    재귀

    @param num: (0, 20]
    '''
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibonacci(num-1)+fibonacci(num-2)


print(fibonacci(int(input())))
