#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # initialize source-destination hashtable
    trip_dict = {}

    # iterate over tickets array...each ticket in the array should become an entry in trip_dict, where source is the key & destination is the value
    for ticket in tickets: 
        trip_dict[ticket.source] = ticket.destination

    # initialize route list...this will be output of destinations in order
    route = [None] * length
    i = 0
    # loop thru & add destinations to route @ index in order
    while i in range(length):
        if route[0] is None: 
            airport = trip_dict["NONE"]
            route[i] = airport
        else:
            airport = trip_dict[route[i-1]]
            route[i] = airport
        i += 1

    return route

