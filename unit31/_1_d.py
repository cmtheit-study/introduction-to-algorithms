from euclid import euclid

def bin_gcd(a: int, b: int):
    res = 1
    while True:
        if b == 0:
            return res * a
        if a == 0:
            return res * b
        if not a & 1:
            if not b & 1:
                a >>= 1
                b >>= 1
                res <<= 1
            else:
                a >>= 1
        else:
            if not b & 1:
                b >>= 1
            else:
                if a > b:
                    a = (a - b) // 2
                else:
                    b = (b - a) // 2

if __name__ == '__main__':
    a = 13 * 18 * 7
    b = 19 * 17 * 18 * 3 * 7
    print(bin_gcd(a, b), euclid(a, b))
