def modular_exponentiation(a: int, b: int, n: int):
    d = 1
    mask = 0x80000000
    while mask:
        d = d * d % n
        if mask & b:
            d = d * a % n
        mask >>= 1
    return d

def modular_exponentiation_rtl(a: int, b: int, n: int):
    d = 1
    mask = 1
    buf = a
    while mask <= 0x80000000:
        if mask & b:
            d = d * buf % n
        buf = buf * buf % n
        mask <<= 1
    return d

if __name__ == '__main__':
    print(modular_exponentiation(94, 13, 700))
    print(modular_exponentiation_rtl(94, 13, 700))
    print(modular_exponentiation_rtl(2, 560, 561))
    print(modular_exponentiation_rtl(3, 560, 561))
