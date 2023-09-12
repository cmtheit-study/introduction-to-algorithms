def euclid(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

if __name__ == '__main__':
    print(euclid(100, 5050))
