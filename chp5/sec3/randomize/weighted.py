import random

def randomize_input(vec: list):
    p = []
    for i in range(len(vec)):
        p.append((i, random.randint(0, len(vec) ** 2)))
    p.sort(key=lambda t: t[1])
    return [vec[i] for (i, w) in p]

vec = [1, 3, 4, 5, 6, 9, 10]

print(randomize_input(vec))