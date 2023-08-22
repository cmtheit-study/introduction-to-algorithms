def between_a_b(arr: list[int], a: int, b: int):
    c = [0 for i in range(a, b + 1)]
    for i in arr:
        if a <= i <= b:
            c[i - a] += 1
    return sum(c)

if __name__ == '__main__':
    a = [1, 1, 1, 1, 2, 2, 4]
    print(between_a_b(a, 1, 3))