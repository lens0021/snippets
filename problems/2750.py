# https://www.acmicpc.net/problem/2750

sorted_list = []

# Do insertion sort
for _ in range(int(input())):
    num = int(input())

    if len(sorted_list) == 0:
        sorted_list.append(num)
        continue

    i = 0
    while i < len(sorted_list) and sorted_list[i] < num:
        i += 1

    sorted_list.insert(i, num)


print(*sorted_list, sep='\n')
