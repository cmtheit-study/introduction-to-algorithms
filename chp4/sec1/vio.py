from ticket import ticket

for in_day in range(ticket.day_len - 1):
    in_price = ticket.get_data(in_day)
    for out_day in range(in_day + 1, ticket.day_len):
        out_price = ticket.get_data(out_day)
        try:
            if out_price - in_price > ticket.earn:
                ticket.set_in_out(in_day, out_day)
        except AttributeError:
            ticket.set_in_out(in_day, out_day)

ticket.report()