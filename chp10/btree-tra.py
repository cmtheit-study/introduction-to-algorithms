class BTree:
    def __init__(self, key, left=None, right=None):
        self.parent = None
        self.key = key
        self.left = left
        if self.left:
            self.left.parent = self
        self.right = right
        if self.right:
            self.right.parent = self

    def tra(self):
        this = self
        new_come = True
        come_from = None
        while True:
            if new_come:
                print(this.key)
                if this.left:
                    this = this.left
                elif this.right:
                    this = this.right
                else:
                    if not this.parent:
                        break
                    new_come = False
                    come_from = this
                    this = this.parent
            else:
                if come_from is this.left:
                    if this.right:
                        new_come = True
                        this = this.right
                    else:
                        if not this.parent:
                            break
                        come_from = this
                        this = this.parent
                elif come_from is this.right:
                    if not this.parent:
                        break
                    come_from = this
                    this = this.parent

btree = BTree(
    18,
    BTree(
        12,
        BTree(7),
        BTree(
            4,
            BTree(5)
        )
    ),
    BTree(
        10,
        BTree(2),
        BTree(21)
    )
)

btree.tra()
