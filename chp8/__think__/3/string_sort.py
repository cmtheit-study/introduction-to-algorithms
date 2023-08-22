def string_sort_inner(arr: list[bytes], a: int, b: int, m: int):
    bits = [0 for i in range(0x101)]
    for i in range(a, b + 1):
        if len(arr[i]) > m:
            bits[arr[i][m] + 1] += 1
        else:
            bits[0] += 1
    for j in range(len(bits) - 1):
        bits[j + 1] += bits[j]
    bits_bp = bits[:]
    res = [None for i in range(a, b + 1)]
    for i in range(b, a - 1, -1):
        if len(arr[i]) > m:
            bits[arr[i][m] + 1] -= 1
            res[bits[arr[i][m] + 1]] = arr[i]
        else:
            bits[0] -= 1
            res[bits[0]] = arr[i]
    arr[a:b + 1] = res[:]
    for i in range(1, len(bits_bp)):
        if bits_bp[i] > bits_bp[i - 1]:
            string_sort_inner(arr, a + bits_bp[i - 1], a + bits_bp[i] - 1, m + 1)

def string_sort(arr: list[bytes]):
    if len(arr) <= 0:
        return
    string_sort_inner(arr, 0, len(arr) - 1, 0)

if __name__ == '__main__':
    import random, string
    strings = [bytes([random.choice(string.ascii_letters).encode('utf-8')[0] for i in range(random.randint(0, 10))]) for i in range(1000)]
    string_sort(strings)
    print(strings)
    for i in range(len(strings) - 1):
        assert strings[i] <= strings[i + 1], (i, strings[i], strings[i + 1])
