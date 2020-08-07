weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
length = 9
limit = 7

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    i = 0
    while i in range(length):
    # for x in weights: 
        j = 0
        while j in range(length) and i is not j:
            x = weights[i]
            
            y = weights[j]
            
            key = ()
            if i >= j: 
                key = (i, j)
            else:
                key = (j, i)
            if key not in cache:
                cache[key] = x + y
            j += 1
        i += 1
    

    for key, value in cache.items():
        if value == limit:
            return list(key)


print(get_indices_of_item_weights(weights, length, limit))