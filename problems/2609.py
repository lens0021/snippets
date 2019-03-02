# https://www.acmicpc.net/problem/2609


def greatest_common_divisor(num1: int, num2: int) -> int:
    if num2 == 0:
        return 0

    # Make sure num1 is greater than num2
    if num2 > num1:
        num2, num1 = num1, num2

    r = num1 % num2
    while r != 0:
        num1, num2 = num2, r
        r = num1 % num2

    return num2


def least_common_multiple(num1: int, num2: int) -> int:
    return (num1*num2)//greatest_common_divisor(num1, num2)


num1, num2 = (int(number) for number in input().split(' '))

print(greatest_common_divisor(num1, num2))
print(least_common_multiple(num1, num2))
