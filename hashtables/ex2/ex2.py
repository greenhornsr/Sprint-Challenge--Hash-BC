#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    index = 0
    for i in hashtable.storage:
        if i is not None:
            node = i
            if node.key is "NONE":
                route[index] = node.value
                hash_table_remove(hashtable, node.key)
                index += 1

            if node.key is route[(index-1)]:
                route[index] = node.value
                index += 1

            if node.key is not route[(index-1)]: 
                match_source = hash_table_retrieve(hashtable, node.value)
                if not match_source:
                    print(f"No such destination flight with source(key) of {node.value}!")
                else:
                    route[index] = match_source
                    index += 1

    # print("our current route: ", route)   
    print("route should be: ", ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP","SLC", "PIT", "ORD"])
    list = [el for el in route if el is not "NONE"]
    print(list)
    return list

# CLI Testing
t1 = Ticket("PIT", "ORD")
t2 = Ticket("XNA", "SAP")
t3 = Ticket("SFO", "BHM")
t4 = Ticket("FLG", "XNA")
t5 = Ticket("NONE", "LAX")
t6 = Ticket("LAX", "SFO")
t7 = Ticket("SAP", "SLC")
t8 = Ticket("ORD", "NONE")
t9 = Ticket("SLC", "PIT")
t10 = Ticket("BHM", "FLG")

tickets = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
length = len(tickets)

reconstruct_trip(tickets, length)