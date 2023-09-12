from random import randint
from euclid import euclid

def pollard_rho(n: int, max: int = 64):
    i = 1
    x_i_1 = 2
    y = x_i_1
    k = 2
    while True:
        i += 1
        x_i = (x_i_1 ** 2 - 1) % n
        d = euclid(y - x_i, n)
        if d != 1 and d != n:
            print(i, d)
            if i > max:
                break
        if i == k:
            y = x_i
            k *= 2
        x_i_1 = x_i

if __name__ == '__main__':
    pollard_rho(19 * 73)


