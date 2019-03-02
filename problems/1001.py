# 숫자 입력받아 빼서 출력하기

line = input()
a, b = [int(str) for str in line.split(' ')]
print(a - b)
