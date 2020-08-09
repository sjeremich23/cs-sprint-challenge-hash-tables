#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.next = None


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # place each ticket in cache with next
    cache = {}
    for ticket in tickets:
        ticket.next = ticket.destination
        cache[ticket.source] = ticket. next

    route = []
    # loop list
    current = cache["NONE"]
    # append to route list
    for i in range(length):
        # append route
        route.append(current)
        # increment next
        current = cache[current]

    return route
