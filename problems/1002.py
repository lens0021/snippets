# import math
# We don't use math.sqrt() to avoid float comparing


def find_number_of_intersections(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> int:
    dis_to_power_of_two = (x2-x1)**2 + (y2-y1)**2
    if dis_to_power_of_two == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        # dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        # 외접
        # r1+r2 == math.sqrt((x2-x1)**2 + (y2-y1)**2)
        if (r1+r2)**2 == dis_to_power_of_two:
            return 1
        # 내접
        # abs(r2-r1) == math.sqrt((x2-x1)**2 + (y2-y1)**2)
        elif (r2-r1)**2 == dis_to_power_of_two:
            return 1
        # 먼 경우
        elif (r1+r2)**2 < dis_to_power_of_two:
            return 0
        # 두 점에서 만나는 경우
        elif (r1+r2)**2 > dis_to_power_of_two > (r2-r1)**2:
            return 2
        # 안에 들어간 경우
        elif (r2-r1)**2 > dis_to_power_of_two:
            return 0
        else:
            return -2


number_of_cases = int(input())
for _ in range(number_of_cases):
    print(find_number_of_intersections(
        *[int(number) for number in input().split(' ')]
    ))
