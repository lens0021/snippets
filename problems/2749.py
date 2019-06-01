# https://www.acmicpc.net/problem/2749


def fib(num: int):
    '''
    @param num: A Natural number in range [1, 1000000000000000000]
    '''
    if num <= 1:
        return num

    def multiplication(matrix1, matrix2):
        '''
        matrix
        a1, b1      a2, b2
        c1, d1      c2, d2
        '''

        a1, b1, c1, d1 = matrix1
        a2, b2, c2, d2 = matrix2

        return (a1*a2+b1*c2, a1*b2+b1*d2, c1*a2+d1*c2, c1*b2+d1*d2)

    def power(matrix, n):
        '''matrix'''

        if n == 0:
            return (1, 0, 0, 1)
        if n == 1:
            return matrix
        if n == 2:
            return multiplication(matrix, matrix)

        if n % 2 == 0:
            half = power(matrix, n//2)
            return multiplication(half, half)
        else:
            half_and_less = power(matrix, n//2)
            return multiplication(multiplication(half_and_less, half_and_less), matrix)

    '''
                       n-1
     fib(n)        1 1     1
    (         ) = (   )   ( )
     fib(n-1)      1 0     0
    '''

    return power((1, 1, 1, 0), num-1)[0]


print(fib(int(input()) % 1500000) % 1000000)
