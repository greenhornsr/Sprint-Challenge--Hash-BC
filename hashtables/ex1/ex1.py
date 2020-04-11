#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    i = 0
    # weights.sort(reverse=True)
    print("weights", weights)
    for weight in weights:
        hash_table_insert(ht, weight, i)
        i += 1


    # check_HT_storage(ht)

    for i in ht.storage:
        if i is not None:
            node = i
            result = limit-node.key
            # print("node.key is: ", node.key)
            print(f"result of {limit}-{node.key} is: ", result)
            answer = hash_table_retrieve(ht, result)
            print("answer is: ", answer)

            if result is weights[0]:
                print("TRUE!!")
                answer = 0

            if answer is not None:
                print("result: ", result)
                print("answer: ", answer, "node.value: ", node.value)
                print("node.key: ", node.key)
                print("node.value: ", node.value)
                print("weights [i]: ", weights[i.value])
                print("weights[answer]: ", weights[answer])
                low = min(answer, node.value)

                if low is node.value:
                    print("low return: ", answer, node.value)
                    return (answer, node.value)
                else: 
                    print("high return: ", result, node.value)
                    return (node.value, answer)
            # else: 
            #     print("no luck, trying again.")
    print('NONE')
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


weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

get_indices_of_item_weights(weights, length, limit)
