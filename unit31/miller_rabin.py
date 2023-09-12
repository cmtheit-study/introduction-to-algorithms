from modular_exponentiation import modular_exponentiation
from random import randint

"""
返回 True 则 n 必为合数，否则无法确定 n 是否为合数。
"""
def witness(a: int, n: int):
    if not n:
        return True
    t = 0
    u = n - 1
    while not u & 1:
        u >>= 1
        t += 1
    x_i_1 = modular_exponentiation(a, u, n)
    if x_i_1 == n - 1 or x_i_1 == 1:
        return False
    for i in range(t):
        x_i = x_i_1 ** 2 % n
        if x_i == n - 1 and i != t - 1:
            return False
        # x_i_1 ≠ ±1 (mod n)
        if x_i == 1:
            return True
        x_i_1 = x_i
    return x_i_1 != 1

def miller_rabin(n: int, s: int):
    for i in range(s):
        a = randint(1, n - 1)
        if witness(a, n):
            return True
    return False

if __name__ == '__main__':
    for i in range(1, 561):
        if not witness(i, 561):
            print(i)
    m = []
    for i in range(100):
        t = 0
        for i in range(561):
            if not miller_rabin(561, 1):
                t += 1
        m.append(t)
    # 约为 10，正好为 Z*(561) 的一个子群大小
    print(sum(m) / len(m))
