def extended_euclid(a: int, b: int):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid(b, a % b)
        return d, y, x - y * (a // b)

if __name__ == '__main__':
    print(extended_euclid(100, 5050))
    print(extended_euclid(35, 3)[1] % 3)
    print(extended_euclid(21, 5)[1] % 5)
    print(extended_euclid(15, 7)[1] % 7)