from c import weighted_mid

class Pos:
    def __init__(self, x: int, weight: float):
        self.x = x
        self.weight = weight
    def __str__(self):
        return f"<{self.x}, {self.weight}>"

# TODO: 代码存疑
def post_pos(pos: list[Pos]):
    return weighted_mid(pos, lambda p: p.weight)

if __name__ == '__main__':
    P = [
        Pos(0, 0.1),
        Pos(1, 0.35),
        Pos(2, 0.05),
        Pos(3, 0.1),
        Pos(3, 0.15),
        Pos(4, 0.05),
        Pos(5, 0.2)
    ]
    print(post_pos(P))
