def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # cache = []
    # for array in arrays:
    #     for value in array:
    #         if value not in cache:
    #             cache.append(value)
    #         else:
    #             return cache

    cache = []

    for i, array in enumerate(arrays):
        print(i, array)
        for i, elem in enumerate(array):
            print(i, elem)
            if elem not in cache:
                cache[elem] = []

            cache[elem].append[i]

    return cache
        

print(intersection([
        [1,2,4],
        [1, 2, 4],
        [1,6,7]]))
    


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
