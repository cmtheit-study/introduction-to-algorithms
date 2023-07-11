from ticket import ticket, Ticket

class TicketDelta(Ticket):
    def __init__(self):
        super().__init__(ticket.data)
        deltas = []
        for i in range(1, ticket.day_len):
            deltas.append(ticket.get_data(i) - ticket.get_data(i - 1))
        self.deltas = deltas

    @property
    def delta_len(self):
        return len(self.deltas)

    @property
    def tot(self):
        tot = 0
        for i in range(self.in_delta, self.out_delta + 1):
            tot += self.deltas[i]
        return tot

    def get_delta(self, delta):
        return self.deltas[delta]

    @property
    def in_delta(self):
        return self.in_day

    @property
    def out_delta(self):
        return self.out_day - 1

    def set_in_out_delta(self, in_delta, out_delta):
        self.set_in_out(in_delta, out_delta + 1)

ticket_delta = TicketDelta()

if __name__ == '__main__':
    for i in range(ticket_delta.delta_len):
        tot = 0
        for j in range(i, ticket_delta.delta_len):
            tot += ticket_delta.get_delta(j)
            try:
                if tot > ticket_delta.tot:
                    ticket_delta.set_in_out_delta(i, j)
            except AttributeError:
                ticket_delta.set_in_out_delta(i, j)
    ticket_delta.report()