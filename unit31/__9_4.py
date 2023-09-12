# unresolved
from euclid import euclid

def solution(n: int, max: int = 64):
    i = 1
    x_i_1 = 2
    y = x_i_1
    product = x_i_1
    k = 2
    while True:
        i += 1
        x_i = (x_i_1 ** 2 - 1) % n
        product = product * (y - x_i) % n
        if i == k:
            d = euclid(product, n)
            if d != 1 and d != n:
                print(i, d)
                if i > max:
                    break
            product = 1
            y = x_i
            k *= 2
        x_i_1 = x_i

if __name__ == '__main__':
    solution(19 * 73)


