# 숫자 입력받아 더해서 출력하기

line = input()
nums = [int(str) for str in line.split(' ')]
summation = sum(nums)
print(summation)
