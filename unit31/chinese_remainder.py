from functools import reduce
from modular_linear_equation_solver import modular_linear_equation_solver

"""
中国余数，求多个质数
"""
def chinese_remainder(*remainders: tuple[int, int]):
    n = reduce(lambda t, s: s * t, [n for n, _ in remainders])
    ms = [n // n_i for n_i, _ in remainders]
    ms_1 = [next(modular_linear_equation_solver(ms[i], 1, remainders[i][0])) for i in range(len(remainders))]
    return sum([(remainders[i][1] * ms[i] * (ms_1[i] % remainders[i][0])) for i in range(len(remainders))]) % n

if __name__ == '__main__':
    print(chinese_remainder((3, 2), (5, 3), (7, 2)))
    print(chinese_remainder((5, 2), (13, 3)))
    n_1 = 5
    n_2 = 13
    for i in range(n_1):
        if not i:
            print(' ', end=' ')
            for j in range(n_2):
                print('{:2}'.format(j), end=' ')
        print()
        print('{}'.format(i), end=' ')
        for j in range(n_2):
            print('{:2}'.format(chinese_remainder((n_1, i), (n_2, j))), end=' ')
    print()
    print(chinese_remainder((5, 4), (11, 5)))
    print(chinese_remainder((9, 1), (8, 2), (7, 3)))
