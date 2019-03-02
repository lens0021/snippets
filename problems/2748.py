# https://www.acmicpc.net/problem/2748


def fibonacci(num: int):
    '''
    @param num: A Natural number in range [1, 90]
    '''
    if num <= 1:
        return num

    memos = [0, 1, None]

    now = 2
    while True:
        remainder = now % 3
        if remainder == 0:
            memos[0] = memos[1] + memos[2]
        elif remainder == 1:
            memos[1] = memos[0] + memos[2]
        elif remainder == 2:
            memos[2] = memos[0] + memos[1]

        if now == num:
            return memos[remainder]
        now += 1


print(fibonacci(int(input())))
