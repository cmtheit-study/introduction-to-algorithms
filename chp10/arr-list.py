from typing import Optional

class ArrList:
    def __init__(self, len: int, keys=[], prev=[], next=[], free=-1, head=-1):
        self.keys = keys if keys else [i for i in range(len)]
        self.prev = prev if prev else [(i - 1 if i else None) for i in range(len)]
        self.next = next if next else [(i + 1 if i != len - 1 else None) for i in range(len)]
        self.free = free if free != -1 else 0
        self.head = head if head != -1 else None

    def alloc(self) -> Optional[int]:
        re = self.delete(self.free)
        if re is not None:
            self.free = re[0]
            self.prev[self.free] = None
            return re[1]

    def insert(self, idx: int):
        if self.head is not None:
            self.prev[self.head] = idx
        self.next[idx] = self.head
        self.prev[idx] = None
        self.head = idx

    def delete(self, head) -> Optional[tuple[
            Optional[int],  # 新的 head 值
            Optional[int],  # 删除的下标
    ]]:
        if head is not None:
            return self.next[head], head

    def exchange(self, idx1, idx2):
        self.prev[idx1], self.prev[idx2] = self.prev[idx2], self.prev[idx1]
        self.next[idx1], self.next[idx2] = self.next[idx2], self.next[idx1]
        self.keys[idx1], self.keys[idx2] = self.keys[idx2], self.keys[idx1]

    def compactify(self):
        ptr = [*range(len(self.next))]
        rtp = [*range(len(self.next))]
        # h 指向当前节点真正的下标
        h = self.head
        i = 0
        while h is not None:
            h = ptr[h]
            self.exchange(h, i)
            rtp[i], rtp[h] = rtp[h], rtp[i]
            ptr[rtp[i]], ptr[rtp[h]] = ptr[rtp[h]], ptr[rtp[i]]
            h = self.next[i]
            i += 1
        for n in range(len(self.next)):
            self.next[n] = ptr[self.next[n]] if self.next[n] is not None else None
            self.prev[n] = ptr[self.prev[n]] if self.prev[n] is not None else None

        self.head = 0 if self.head is not None else None
        self.free = ptr[self.free] if self.free is not None else None

    def __str__(self):
        return f'''head: {self.head}, free: {self.free}
keys: [{', '.join(str(j) for j in ["{:4}".format(i) if i is not None else None for i  in self.keys])}]
prev: [{', '.join(str(j) for j in ["{:4}".format(i) if i is not None else None for i  in self.prev])}]
nxet: [{', '.join(str(j) for j in ["{:4}".format(i) if i is not None else None for i in self.next])}]'''

if __name__ == '__main__':
    a = ArrList(8,
                [2, 4, 1, 3, 16, 5, 9, 6],
                [5, 4, 1, None, 6, 7, None, 3],
                [None, 2, None, 7, 1, 0, 4, 5], 3, 6)
    print(a)
    a.compactify()
    print(a)