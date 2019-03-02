# https://www.acmicpc.net/problem/1003
# 피보나치를 단순히 재귀할 때 fib(0)과 fib(1)이 몇번 호출되는지 구하기

number_of_cases = int(input())
cases = []
for _ in range(number_of_cases):
    cases.append(int(input()))

max_case = max(cases)

call_of_0, call_of_1 = [1, 0], [0, 1]

if max_case > 2:
    for number in range(2, max_case+1):
        call_of_0.append(call_of_0[number-1] + call_of_0[number-2])
        call_of_1.append(call_of_1[number-1] + call_of_1[number-2])

for index in range(number_of_cases):
    number = cases[index]

    print(f'{call_of_0[number]} {call_of_1[number]}')
