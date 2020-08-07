def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # initialize cache
    cache = {}

    # loop thru and add numbers together...add sums to cache if not already in there...make sure key is of index in order of larger to smaller
    i = 0
    while i in range(length): 
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
    
    # return a list of the indices (which is the key) if the sum (value) is the limit
    for key, value in cache.items():
        if value == limit:
            return list(key)
