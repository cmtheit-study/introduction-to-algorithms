from random import randint

def random():
    return randint(0, 1)

def rand(a, b):
    rg = b - a + 1
    if rg == 1:
        return a
    if rg & 1:
        while True:
            res = rand(a, b + 1)
            if res != b + 1:
                return res
    else:
        if random():
            return rand(a, (a + b) // 2)
        else:
            return rand((a + b) // 2 + 1, b)


all = [0, 0, 0, 0]
for i in range(40000):
    all[rand(0, len(all) - 1)] += 1
print(all)

