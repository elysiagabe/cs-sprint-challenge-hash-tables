def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # initialize dictionary to keep track of occurence of numbers
    number_count = {}

    # loop thru outer array
    for inner_arr in arrays: 
        # remove any dups from the inner arrray
        inner_arr = list(dict.fromkeys(inner_arr))
        # loop thru each inner array
        for num in inner_arr: 
            # if number doesn't exist in dictionary, add it with count 1
            if num not in number_count:
                number_count[num] = 1
            # if it does, increment the count
            else: 
                number_count[num] += 1
    
    # initialize result list
    result = []

    # add the key to result of any number that has a count that's equal to the length of the outer array (this should mean it showed up in each inner array)
    for num, count in number_count.items():
        if count == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
