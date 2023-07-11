class Ticket:
    def __init__(self, data: list):
        self.data = data

    def set_in_out(self, in_day, out_day):
        self.in_day = in_day
        self.out_day = out_day

    @property
    def day_len(self):
        return len(self.data)

    @property
    def earn(self):
        return self.get_data(self.out_day) - self.get_data(self.in_day)

    def get_data(self, day):
        return self.data[day]

    def report(self):
        if hasattr(self, 'in_day'):
            print(f"在第 {self.in_day} 天买入，第 {self.out_day} 天卖出，挣得 {self.earn}.")
        else:
            print("未设置买入卖出时间。")

data = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

ticket = Ticket(data)

__all__ = ('ticket', )