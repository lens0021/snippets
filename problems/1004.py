# https://www.acmicpc.net/problem/1004
# 원으로 표현된 항성계를 여행하는 어린왕자
number_of_test_cases = int(input())


def is_in_circle(coord, circle):
    x, y = coord
    cx, cy, r = circle

    if (cx-x)**2 + (cy-y)**2 < r**2:
        return True
    return False


for _ in range(number_of_test_cases):
    coords = [int(number) for number in input().split(' ')]
    start, end = coords[0:2], coords[2:4]

    number_of_circles = int(input())
    circles = []
    for _ in range(number_of_circles):
        circles.append([int(number) for number in input().split(' ')])

    count = 0
    for circle in circles:
        if is_in_circle(start, circle) != is_in_circle(end, circle):
            count += 1
    print(count)
