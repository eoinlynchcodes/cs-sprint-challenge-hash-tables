def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    result = []

    for weight in weights:
        for another in weights:
            if weight + another == limit:
                result.append(weight)
                result.append(another)
                result.sort(reverse=True)
                return result


print(get_indices_of_item_weights([1, 2], 4, 3))

