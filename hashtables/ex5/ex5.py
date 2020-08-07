# Your code here
my_files = ["appl/e", "banan/a", "carrot", "do/g", "do/o/doo"]

my_queries = ["appl", "do"]

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # initialize query cache
    query_dict = {}

    # add each query in queries list to array (value doesn't really matter here)
    for query in queries:
        query_dict[query] = 1
    
    # initialize result list
    result = []

    # loop thru files
    for file in files: 
        # filename (what's being searched for) is substring after the last "/"...need to split string on "/" as separator...then return last substring after splitting
        file_name = file.split("/")[-1]

        # check if file name is in query_dict...if it is, append that file path to result list
        if file_name in query_dict:
            result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
