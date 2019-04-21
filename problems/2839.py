# https://www.acmicpc.net/problem/2839

# load = int(input())

# k == 3x + 5y일 때 x+y의 최솟값을 구하라(단 k는 자연수, x와 y는 0 혹은 양의 정수, 3<=k<=5000)
# 불가능하면 -1 출력..

time = (5001-4553+1)//8
index = 7
rng = range(4553+time*index, 4553+time*(index)+time)

for k in rng:
    results = []
    for x in range(0, k+1):
        for y in range(0, k+1):
            if x*3 + y*5 == k:
                results.append(x+y)
    print('k == '+str(k)+':', end='')
    print(min(results) if results else -1)
