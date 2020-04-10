#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    results = []
    
    i = 0
    for weight in weights:
        hash_table_insert(ht, weight, i)
        i += 1
        results.append(limit-weight)

    check_HT_storage(ht)

    for i in ht.storage:
        if i is not None:
            node = i
            result = limit-node.key
            # print("node.key is: ", node.key)
            # print(f"result of {limit}-{node.key} is: ", result)
            answer = hash_table_retrieve(ht, result)
            if answer is not None:
                # print("result: ", result)
                # print("answer: ", answer, node.value)
                # print("node.key: ", node.key)
                # print("node.value: ", node.value)
                low = min(result, node.key)
                high = max(result, node.key)
                # print("low: ", low, ", high: ", high)
                return (high, low)
            # else: 
            #     print("no luck, trying again.")
    return None

def check_HT_storage(ht):
    for i in ht.storage:
        if i is not None:
            node = i
            print("KEY - Post Insert ht Storage:  ", node.key)
            print("VALUE - Post Insert ht Storage:  ", node.value)
        else: 
            print("this is HT storage: ", i)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# weights = [ 4, 6, 10, 15, 16 ]
weights = [ 2, 4, 4, 6, 10, 15, 16, 20 ]
length = 5
limit = 21

get_indices_of_item_weights(weights, length, limit)
