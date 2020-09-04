#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    '''
    tackes in class object of ticket, and lentht of tickets
    '''
    cache = {}

    # Build the cache
    for ticket in tickets:
        if ticket.source is None:
            cache['NONE'] = ticket.destination
        if ticket.destination is None:
            cache[ticket.source] = 'NONE'

        cache[ticket.source] = ticket.destination

    # Build the ordered list of tickets
    ticket_list = []
    switch = True
    source = 'NONE'
    while switch is True:
        dest = cache[source]
        source = dest
        ticket_list.append(dest)
        if dest == 'NONE':
            switch = False

    return ticket_list


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)