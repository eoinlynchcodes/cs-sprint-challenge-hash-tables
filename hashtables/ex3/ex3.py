def intersection(arrays):
    """
    YOUR CODE HERE
    """

    cache = {}
    intersection = []
    for array in arrays:
        for item in array:
            if item in cache:
                cache[item] += 1
            else:
                cache[item] = 1

    for item in cache:
        if cache[item] == len(arrays):
            intersection.append(item)

    return intersection

            # Increment the index. Keep searching
    # items that are in the array and the cache are returned.



        

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
