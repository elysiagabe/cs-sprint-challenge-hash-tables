def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # first remove any duplicates from the list just in case
    a = list(dict.fromkeys(a))

    # then make every number in the no dups list positive
    b = []
    for x in a:
        if x < 0:
            x = -x
        b.append(x)

    # then create a dictionary to count number occurrences 
    num_count = {}

    for num in b:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

    # if number shows up more than once (should be twice...), that means there were initially pos/neg corresponding nums...add to result list
    result = []

    for num, count in num_count.items():
        if count > 1:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
