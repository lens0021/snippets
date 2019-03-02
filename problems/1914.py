# https://www.acmicpc.net/problem/1914

number_of_disks = int(input())


def solution(number_of_disks, from_peg, to_peg, temp_peg):
    if number_of_disks == 1:
        print(str(from_peg)+' '+str(to_peg))
        return

    solution(number_of_disks-1, from_peg, temp_peg, to_peg)
    print(str(from_peg)+' '+str(to_peg))
    solution(number_of_disks-1, temp_peg, to_peg, from_peg)


print(2**number_of_disks-1)
if number_of_disks <= 20:
    solution(number_of_disks, 1, 3, 2)
