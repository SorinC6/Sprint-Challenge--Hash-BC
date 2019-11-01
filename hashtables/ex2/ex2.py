#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert ticket into hashtable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # find and make NONE the first element
    route[0] = hash_table_retrieve(hashtable, "NONE")

    # map and retrive the route
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])
    return route
